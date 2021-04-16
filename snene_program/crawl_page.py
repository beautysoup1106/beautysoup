from snene_program import asyncio_program

# def main():
#     url = 'https://movie.douban.com/cinema/later/beijing/'
#     init_page = requests.get(url, headers={'User-Agent': 'test'}).content
#     init_soup = BeautifulSoup(init_page, 'lxml')
#
#     all_movies = init_soup.find('div', id='showing-soon')
#
#     for each_movie in all_movies.find_all('div', class_='item'):
#         all_a_tag = each_movie.find_all('a')
#         all_li_tag = each_movie.find_all('li')
#
#         movie_name = all_a_tag[1].text
#         url_to_fetch = all_a_tag[1]['href']
#         movie_date = all_li_tag[0].text
#
#         response_item = requests.get(url_to_fetch, headers={'User-Agent': 'test'}).content
#         soup_item = BeautifulSoup(response_item, 'lxml')
#         img_tag = soup_item.find('img')
#
#         print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))
#
#
# main()

'''
协程方式爬
'''


# async def fetch_content(url):
#     async with aiohttp.ClientSession(
#             headers={'User-Agent': 'test'}, connector=aiohttp.TCPConnector(ssl=False)
#     ) as session:
#         async with session.get(url) as response:
#             return await response.text()
#
#
# async def main():
#     url = 'https://movie.douban.com/cinema/later/beijing/'
#     init_page = await fetch_content(url)
#     init_soup = BeautifulSoup(init_page, 'lxml')
#
#     movie_names, url_to_fetch, movie_dates = [], [], []
#
#     all_movies = init_soup.find('div', id='showing-soon')
#     for each_movie in all_movies.find_all('div', class_='item'):
#         all_a_tag = each_movie.find_all('a')
#         all_li_tag = each_movie.find_all('li')
#
#         movie_names.append(all_a_tag[1].text)
#         url_to_fetch.append(all_a_tag[1]['href'])
#         movie_dates.append(all_li_tag[0].text)
#
#     tasks = [fetch_content(url) for url in url_to_fetch]
#     pages = await asyncio.gather(*tasks, return_exceptions=True)
#
#     for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
#         soup_item = BeautifulSoup(page, 'lxml')
#         img_tag = soup_item.find('img')
#
#         print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))
#
#
# asyncio.run(main())

'''
协程实现回调函数
python3.7及以上的版本，对task调用add_done_callback()函数，即可绑定特定的
回调函数。回调函数接收一个future对象，可以通过future.result()来获取协程函数的返回值
'''


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio_program.sleep(sleep_time)
    return 'OK {}'.format(url)


async def main(urls):
    tasks = [asyncio_program.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        task.add_done_callback(lambda future: print('result:', future.result()))

    await asyncio_program.gather(*tasks, return_exceptions=True)

asyncio_program.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
