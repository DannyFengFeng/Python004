
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#加入cookie有效
header = {
    'Cookie':'89095844.1600956169792.1601097855082.1601097868144.5; uuid_n_v=v1; uuid=A04B5290FE6E11EAB86FCBED18BA04EA139452708179446D89B104ECF144A1E6; _csrf=49698956a3d441ac80645c60583a29bdd5157dfee8f462eaf01f8e585522caff; _lxsdk_cuid=174c06c78b4c8-01c8844a73ae1c-333769-144000-174c06c78b5c8; _lxsdk=A04B5290FE6E11EAB86FCBED18BA04EA139452708179446D89B104ECF144A1E6; mojo-uuid=796ba0d7c2f8481097e67e1f16d03000; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1600956168,1600956217,1601096984,1601097855; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-session-id={"id":"32e1eb8bc038f23146d32b4348d96bae","time":1601173754840}; mojo-trace-id=12; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601174895; __mta=89095844.1600956169792.1601097868144.1601174895806.6; _lxsdk_s=174cd6493be-398-cf9-fe7%7C%7C16',
    'user-agent':user_agent}

# myurl='https://maoyan.com/'
myurl='https://maoyan.com/films?showType=3'
response=requests.get(myurl,headers=header)

bs_info=bs(response.text,'html.parser')

# print(response.text)
# print(f'返回码是：{response.status_code}')

print(response.status_code)
# print(bs_info)
for tags in bs_info.find_all('dd',):
    name_list = []
    type_list = []
    time_list=[]
    for tag1 in tags.find_all('a',):
        for detail_movie in tag1.find_all('div',attrs={"class":'movie-hover-title'}):
            count_name=0
            for name_movie in detail_movie.find_all('span',attrs={'class':'name'}):
                name_list.append(name_movie.text)
                if len(name_list) >=10:
                    break
            for movies in detail_movie.find_all('span',):
                # print(movies)
                if(movies.text=="类型:"):
                    type_movie=detail_movie.text
                    type_list.append(type_movie.split('\n')[2].strip())
                if (movies.text == "上映时间:"):
                    # print(detail_movie)
                    time_movie = detail_movie.text
                    time_list.append(time_movie.split('\n')[2].strip())
                # print(movies.text)
            if len(name_list) >= 10:
                break
            #     count=1
        if len(name_list) >= 10:
            break
    print(name_list)
    print(type_list)
    print(time_list)
    if len(name_list) >= 10:
        break
mylist=[name_list,type_list,time_list]
movies=pd.DataFrame(data=mylist)
movies.to_csv('./movies.csv',encoding='utf8',index=False,header=False)


