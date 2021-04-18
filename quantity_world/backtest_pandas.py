import abc
import os.path as path
from numbers import Number
from typing import Callable

import pandas as pd
import numpy as np


def assert_message(condition, msg):
    if not condition:
        raise Exception(msg)


def read_file(filename):
    # 获取文件绝对路径
    filepath = path.join(path.dirname(__file__), filename)

    # 判断文件是否存在
    assert_message(path.exists(filepath), '文件不存在2')

    # 读取CSV文件并返回
    return pd.read_csv(filepath,
                       index_col=0,
                       parse_dates=True,
                       infer_datetime_format=True)


# BTCUSD = read_file('BTCUSD_GEMINI.csv')
# assert_message(BTCUSD.__len__() > 0, '读取失败')
# print(BTCUSD.head())


def SMA(values, n):
    '''
    返回简单滑动平均
    '''
    return pd.Series(values).rolling(n).mean()


def crossover(series1, series2):
    '''
    检查两个序列是否在结尾交叉
    '''
    return series1[-2] < series2[-2] and series1[-1] > series2[-1]


class Strategy(metaclass=abc.ABCMeta):
    '''
    抽象策略类，用于定义交易策略。
    如果要定义自己的策略类，需要继承这个基类，并实现两个抽象方法
    strategy.ini
    strategy.next
    '''

    def __init__(self, broker, data):
        '''
        构造策略对象
        1：ExchangeAPI类型，交易API接口，用于模拟交易
        2：list类型，行情数据
        '''

        self._indicators = []
        self._broker = broker
        self._data = data
        self._tick = 0

    def I(self, func: Callable, *args):
        '''
        计算买卖指标向量。买卖指标向量是一个数组，长度和历史数据对应，用于判定这个时间点上
        需要进行买还是卖
        例如计算滑动平均：
        def init():
            self.sma=self.I(utils.SMA,self.data.Close,N)
        '''
        value = func(*args)
        value = np.asarray(value)
        assert_message(value.shape[-1] == len(self._data.Close),
                       '指标器长度必须和data长度相同')
        self._indicators.append(value)

        return value

    @property
    def tick(self):
        return self._tick

    @abc.abstractmethod
    def init(self):
        '''
        初始化策略。在策略回测/执行过程中调用一次，用于初始化策略内部状态
        这里也可以预计算策略的辅助参数，比如根据历史行情数据，计算买卖的
        指示器向量
        训练模型/初始化模型参数
        '''
        pass

    @abc.abstractmethod
    def next(self, tick):
        '''
        步进函数，执行第tick步的策略。tick代表当前的“时间”。
        比如data[tick]用于访问当前的市场价格
        '''
        pass

    def buy(self):
        self._broker.buy()

    def sell(self):
        self._broker.sell()

    @property
    def data(self):
        return self._data


class SmaCross(Strategy):
    # 小窗口SMA的窗口大小，用于计算SMA快线
    fast = 10

    # 大窗口SMA的窗口大小，用于计算SMA慢线
    slow = 20

    def init(self):
        # 计算历史上每个时刻的快线和慢线
        self.sma1 = self.I(SMA, self.data.Close, self.fast)
        self.sma2 = self.I(SMA, self.data.Close, self.fast)

    def next(self, tick):
        # 如果此时快线刚好越过慢线，买入全部
        if crossover(self.sma1[:tick], self.sma2[:tick]):
            self.buy()

        # 如果是慢线刚好越过快线，卖出全部
        elif crossover(self.sma2[:tick], self.sma1[:tick]):
            self.sell()

        # 否则，这个时刻不执行任何操作

        else:
            pass


class ExchangeAPI:
    def __init__(self, data, cash, commision):
        assert_message(0 < cash, '初始现金数量大于0，输入的现金数量：{}'.format(cash))
        # assert_message((0 <= commision <= 0.05, '合理的手续费一般不会超过5%，输入的费率：{}'.format(commision)))

        self._initial_cash = cash
        self._data = data
        self._commision = commision
        self._position = 0
        self._cash = cash
        self._i = 0

    @property
    def cash(self):
        '''
        返回当前账户现金数量
        '''
        return self._cash

    @property
    def position(self):
        '''
        返回当前账户仓位
        '''
        return self._position

    @property
    def initial_cash(self):
        '''
        返回初始现金数量
        '''
        return self._initial_cash

    @property
    def current_price(self):
        '''
        返回当前市场价格
        '''
        return self._data.Close[self._i]

    @property
    def market_value(self):
        '''
        返回当前市值
        '''
        return self._cash + self._position * self.current_price

    def buy(self):
        '''
        用当前账户剩余资金，按照市场价格全部买入
        '''
        self._position = float(self._cash / (self.current_price * (1 + self._commision)))
        self._cash = 0.0

    def sell(self):
        '''
        卖出当前账户剩余持仓
        '''

        self._cash += float(self._position * self.current_price * (1 - self._commision))
        self._position = 0.0

    def next(self, tick):
        self._i = tick


class Backtest:
    """
    Backtest回测类，用于读取历史行情数据、执行策略、模拟交易并估计收益
    初始化的时候调用Backtest.run来回测
    instance or ‘backtesting.backtesting.Backtest.optimize' to
    optimize it
    """

    def __init__(self,
                 data: pd.DataFrame,
                 strategy_type: type(Strategy),
                 broker_type: type(ExchangeAPI),
                 cash: float = 10000,
                 commission: float = .0):
        """
        构造回测对象。需要的参数包括：历史数据，策略对象，初始资金数量，手续费率等
        初始化过程包括检测输入类型，填充数据空值等。
        参数
        1：pandas DataFrame格式的历史OHLCV数据
        2:交易所API类型，负责执行买卖操作以及账户状态的维护
        3：策略类型
        4；初始资金数量
        5：每次交易手续费率。
        """
        assert_message(issubclass(strategy_type, Strategy), 'strategy_type不是一个Strategy类型')
        assert_message(issubclass(broker_type, ExchangeAPI), 'broker_type 不是一个ExchangeAPI')
        # assert_message(issubclass(commission, Number), 'commission 不是浮点数类型')

        data = data.copy(False)

        # 如果没有Volume列，填充NaN
        if 'Volume' not in data:
            data['Volume'] = np.nan
        # 验证OHLC数据格式
        assert_message(len(data.columns & {
            'Open', 'High', 'Low', 'Close', 'Volume'
        }) == 5, ("输入的'data'格式不正确，至少需要包含这些列："
                  "'open','High','Low','Close'"))
        # 检查值缺失
        assert_message(not data[['Open', 'High', 'Low', 'Close']].max().isnull().any(),
                       ('部分OHLC包含缺失值，请去掉那些行或者通过差值填充。'))

        # 如果行情数据没有按照时间排序，重新排序一下
        if not data.index.is_monotonic_increasing:
            data = data.sort_index()

        # 利用数据，初始化交易所对象和策略对象。
        self._data = data
        self._broker = broker_type(data, cash, commission)
        self._strategy = strategy_type(self._broker, self._data)
        self._results = None

    def run(self):
        """
        运行回测，迭代历史数据，执行模拟交易并返回回测结果
        Run the backtest.Return pd.Service with results and statistics
        Keyword arguments are interpreted as strategy parameters
        """

        strategy = self._strategy
        broker = self._broker

        # 策略初始化
        strategy.init()

        # 设定回测开始和结束位置
        start = 100
        end = len(self._data)

        # 回测主循环，更新市场状态，然后执行策略
        for i in range(start, end):
            # 注意要先把市场状态移动到第i时刻，然后再执行策略
            broker.next(i)
            strategy.next(i)
        # 完成策略执行之后，计算结果并返回
        self._results = self._compute_result(broker)
        return self._results

    def _compute_result(self, broker):
        s = pd.Series()
        s['初始市值'] = broker.initial_cash
        s['结束市值'] = broker.market_value
        s['收益'] = broker.market_value - broker.initial_cash
        return s


def main():
    BTCUSD = read_file('BTCUSD_GEMINI.csv')
    ret = Backtest(BTCUSD, SmaCross, ExchangeAPI, 10000.0, 0.03).run()

    print(ret)


if __name__ == '__main__':
    main()
