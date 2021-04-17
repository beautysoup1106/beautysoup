# import json
#
# import requests
#
# gemeni_ticker = 'https://api.gemini.com/v1/pubticker/{}'
# symbol='btcusd'
# btc_data=requests.get(gemeni_ticker.format(symbol)).json()
#
# print(json.dumps(btc_data,indent=4))
#

# 选取要获取的数据时间段
import requests
import pandas as pd
import matplotlib.pyplot as plt

'''
一个基本的交易系统；
    1、行情模块：尝试获取市场的行情数据，通常也负责获取交易账户的状态
    2、策略模块：订阅市场的数据，根据设定的算法发出买、卖的指令给执行模块
    3、执行模块：接受并把策略模块发过来的买、卖指令封装并转发到交易所，同时监督并确保策略买卖的完整执行
python在算法交易领域流行的原因：
    1、numpy和pandas组合，数据分析和数据处理能力
    2、许许多多已经开发成熟的算法交易库，zipline策略回溯，pyfolio组合投资分析，交易所提供了基于python的API客户端
        用户只需要定义策略模块就可以进行算法交易和回测
    3、便利的交易平台：算法交易平台可以执行自定义python策略，无需搭建量化交易框架。算法交易平台，实际上等效于帮
        用户完成了行情模块和执行模块，用户只需要在其中定义策略模块，即可进行算法交易和回测（Quantoppian(基于zipline),
        国内的bigquant、果仁网等
    4、广泛的行业应用
        
    4、
    
'''

periods = '3600'

# 通过HTTP抓取btc历史价格数据
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
                    params={
                        'periods': periods
                    }
                    )
data = resp.json()

print(data)

# 转换成pandas data frame
df = pd.DataFrame(
    data['result'][periods],
    columns=[
        'CloseTime',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'ClosePrice',
        'Volume',
        'NA'
    ]
)
# 输出Dataframe的头部几行
print(df.head())

# 绘制btc价格曲线
df['ClosePrice'].plot(figsize=(3, 7))
plt.show()
