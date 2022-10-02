import pandas as pd
import urllib.request

#from multiprocessing import Process

def Image_download(urls,start_idx,end_idx):
    sliced_url = urls.loc[start_idx : end_idx]

    print(start_idx, end_idx)
    for i in range(start_idx, end_idx+1):
        
        try:
            url = sliced_url.loc[i][1]
            urllib.request.urlretrieve(url, 'afternoon/'+str(i//10000)+'0000/'+str(i)+'.jpg')

            print('i == ',i)
        except:
            continue



if __name__ == '__main__':
    urls = pd.read_csv('afternoon city_urls.csv') ## afternoon city_urls.csv or night_urls.csv

    start_idx = 0
    end_idx   = 1000
    Image_download(urls, start_idx, end_idx)

    '''
    이 밑은 신경안써도됨
    '''

    '''processes = []

    for i in range(1):
        sliced_urls = urls.loc[i*10000:(i+1)*10000-1]
        
        p = Process(target=Image_download, args=[sliced_urls, i])
        p.start()

        processes.append(p)

    for process in processes:
        process.join()'''
