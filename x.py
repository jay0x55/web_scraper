import json
import numpy
import random
import requests
import os
import subprocess
import sys
import time
import threading
from bs4 import BeautifulSoup
from optparse import OptionParser

par = OptionParser()

par.add_option("-b", "--bot", action="store",
               type="int", dest="bot", default=10,
               help="number of bots to start [default :10]")

par.add_option("-c", "--category", action="store_true",
               dest="category", default=False,
               help="enable category mode")
par.add_option("-p", "--populare", action="store_true",
               dest="populare", default=False,
               help="scrap by populare")
par.add_option("-n", "--new", action="store_true",
               dest="new", default=False,
               help="enable newests mode")
par.add_option("-r", "--proxy", action="store",
               type="str", dest="proxy", default="",
               help="use your own proxy list")

par.add_option("-t", "--tor", action="store_true",
               dest="tor", default=False,
               help="use tor proxy")

par.add_option("-m", "--manual", action="store",
               type="str", dest="manual", default="",
               help="use manual link to scrap")

(options, args) = par.parse_args()

url = "https://bartarinha.com"
category = []
sth_ls = []
prx_ls = []


def gt(res):
    s = BeautifulSoup(res.content, "html.parser")
    o = s.find(id="menu")
    ls = []
    for lk in o.findAll('a'):
        if "group" in lk.get('href'):
            ls.append(lk.get("href"))
            category.append(lk.text.strip())
    return ls


def just_k(proxy):
    header = {'User-Agent': random.choice(uagent)}
    res = requests.get(url, proxies=proxy, headers=header)
    return res


def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0")
    uagent.append("Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0")
    uagent.append(
        "Opera/9.80 (Linux armv7l) Presto/2.12.407 Version/12.51 , D50u-D1-UHD/V1.5.16-UHD (Vizio, D50u-D1, Wireless)")
    uagent.append("Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    uagent.append("WeatherReport/1.2.0 CFNetwork/485.13.9 Darwin/11.0.0")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36")
    uagent.append(
        "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    uagent.append(
        "Mozilla/5.0 (Linux; Android 6.0.1; RedMi Note 5 Build/RB3N5C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Linux; Android 9; SM-G965F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36")
    return uagent


def making(lin):
    my_arr = numpy.array(lin)
    last_arr = my_arr.reshape(options.bot, int(len(lin) / options.bot))
    return last_arr


def test(proxy_file=''):
    if proxy_file != '':
        global prx_ls
        test_url = 'http://ifconfig.me/ip'
        print("\n[+] testing proxies...\n")
        prx_file = open(proxy_file, "r")
        for i in prx_file:
            i = i.replace("\n", "")
            try:
                proxy_test = {'http': i, 'https': i}
                requests.get(test_url, headers={'User-Agent': random.choice(uagent)}, proxies=proxy_test, timeout=5)
                print("[+] good proxy ..... [" + i + "]")
                prx_ls.append(i)

            except:
                print("[!] bad proxy ...... [" + i + "]")

        prx_file.close()
        print("\n[>] " + "done")


def nice(ls):
    nm = 0
    with open('category-id.txt', 'w', encoding="u8") as fl:
        for v in ls:
            fl.write(f"[{nm}] {v}\t")
            if nm % 3 == 0:
                fl.write("\n")
            nm += 1


def gallery(ls, title):
    path = os.getcwd()
    want = "/img/" + title + "/gallery/"
    try:
        os.mkdir(path + want)
        px = ""
        if prx_ls:
            px = random.choice(prx_ls)
        for i in ls:
            subprocess.Popen(['curl', i, "-s", "-x", px, "-o", path + want + i.split('/')[-1].split("?")[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass


def checking(data):
    nw = time.gmtime()
    nm = f"{nw.tm_year}.{nw.tm_mon}.{nw.tm_mday}__{nw.tm_hour}:{nw.tm_min}:{nw.tm_sec}.json"
    with open(nm, 'w', encoding='u8') as data_file:
        data_file.write(json.dumps(data, indent=4, ensure_ascii=False))


def dow(ar, jojo):
    path = os.getcwd()
    fi = "/img/" + jojo + "/"
    try:
        os.mkdir(path + fi)
        px = ""
        if prx_ls:
            px = random.choice(prx_ls)
        subprocess.Popen(['curl', ar, "-s", "-x", px, "-o", path + fi + ar.split('/')[-1].split("?")[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass


def srt(hey, proxy):
    for _ in hey:
        with open(".conf/.saved", "r") as rd:
            if _.split("/")[2] in rd.read():
                continue

        with open(".conf/.saved", "a", encoding="u8") as che_file:
            che_file.write(_.split("/")[2] + ",")

        data = {"title": "", "description": "", "product_url": "", "image_url": "", "telegram": "", "instagram": "",
                "whatsapp": "", "website": "", "map_address": [], "telephone": [], "work_times": [], "option": [],
                "tags": [], "views": "", "comments": ""}
        rq = requests.get(url + _, proxies=proxy, headers={'User-Agent': random.choice(uagent)})
        tt = BeautifulSoup(rq.content, "html.parser")
        title = tt.find('meta', property="og:title")
        try:
            data['title'] = title.get('content')
        except AttributeError:
            continue

        des = tt.find('meta', property="og:description")
        data['description'] = des.get("content")
        data['product_url'] = url + _
        mg = tt.find("img", class_="img-responsive")
        dow(url + mg.get('src'), title.get('content'))
        try:
            data['image_url'] = url + mg.get("src")
        except:
            pass

        social = tt.find('div', class_='btn-list')
        for n in social.findAll('a'):
            try:
                ul = n.get('href')
                if 'instagram' in ul:
                    data['instagram'] = ul
                elif 't.me' in ul:
                    data['telegram'] = ul
                elif 'whatsapp' in ul:
                    data['whatsapp'] = ul
                else:
                    data['website'] = ul
            except:
                continue

        maps = tt.find('div', class_='direction-btns')
        map_ls = []
        try:
            for check in maps.findAll('a'):
                try:
                    map_ls.append(check.get('href'))
                except:
                    continue
        except:
            pass

        data['map_address'] = map_ls
        nu = []
        telephone = tt.find('div', class_='phone')
        for tel in telephone.findAll('a'):
            try:
                nu.append(tel.get('href'))
            except:
                continue
        data['telephone'] = nu
        gall_ls = []
        gall = tt.find('div', class_='image-gallery')
        try:
            for gl in gall.findAll('a'):
                try:
                    gall_ls.append(url + gl.get('href'))
                except:
                    continue
        except:
            pass

        gallery(gall_ls, title.get('content'))
        work_ls = []
        work_time = tt.find('div', class_='working-hours')
        con = 0
        for work in work_time.findAll('div'):
            try:
                text = work.text
                text = text.replace('\n', '')
                text = text.replace(' ', '')
                text = text.replace('\r', '')
                if (con == 0) or (con % 4 == 0):
                    work_ls.append(text)
                con += 1
            except:
                continue
        data["work_times"] = work_ls

        options_ls = []
        opti = tt.find('div', class_='amenities-btn')
        try:
            for pucat in opti.findAll('a'):
                options_ls.append(pucat.text)
        except:
            pass

        data['option'] = options_ls

        tag_ls = []
        tags = tt.find('div', class_='keywords')
        try:
            for tg in tags.findAll('a'):
                tag_ls.append(tg.text)
        except:
            pass

        data['tags'] = tag_ls
        view = tt.find('div', class_='view-counter')
        try:
            data['views'] = view.text
        except:
            pass

        comment = tt.find('div', class_='comment')
        try:
            data['comments'] = comment.text
        except:
            pass

        sth_ls.append(data)


def mn(u, num):
    global prx_ls
    proxy = dict(http='', https='')
    threads = list()
    if prx_ls:
        number = random.choice(prx_ls)
        proxy['http'], proxy['https'] = number, number
    print("\nwait to make the requests......")
    req = requests.get(u, proxies=proxy, headers={'User-Agent': random.choice(uagent)})
    b = BeautifulSoup(req.content, "html.parser")
    li = []
    for lnk in b.findAll('a'):
        li.append(lnk.get("href"))

    pl = []
    for gang in li:
        try:
            if "ad" in gang:
                pl.append(gang)
        except TypeError:
            pass
    st = list(set(pl))
    if num == "":
        hey = st
    else:
        hey = st[0:int(num)]

    try:
        arr = making(hey)
    except:
        print("\n[-] error:\n\tbots number didn't match with products number to scrape")
        sys.exit(1)
    if "nt" in os.name:
        os.system("cls")
    else:
        os.system("clear")
    print(f"[+] running:\n\tbots: {options.bot}\n\tdata: {len(hey)}\n\n")
    start = time.time()
    for index in range(options.bot):
        if prx_ls:
            number = random.choice(prx_ls)
            proxy['http'], proxy['https'] = number, number

        x = threading.Thread(target=srt, args=(arr[index], proxy,))
        threads.append(x)
        x.start()

    for i, thread in enumerate(threads):
        thread.join()
    tm = time.time() - start
    print(f"\n\nFinished in: {tm}s\n\n")


def main():
    global prx_ls
    if not os.path.isdir(".conf/"):
        os.mkdir(os.getcwd() + "/.conf/")
        hs = open(".conf/.saved", "w")
        hs.write("")
        hs.close()
    if not os.path.isdir("img/"):
        os.mkdir(os.getcwd() + "/img/")
        hs = open(".conf/.tor", "w")
        hs.write("socks5://127.0.0.1:9050\nsocks5://127.0.0.1:9150\n127.0.0.1:8118")
        hs.close()
    proxy = dict(http='', https='')
    if options.tor:
        test(".conf/.tor")
    else:
        test(options.proxy)

    if prx_ls:
        number = random.choice(prx_ls)
        proxy['http'], proxy['https'] = number, number

    if options.category:
        gngbng = gt(just_k(proxy))
        nice(category)
        ct = input("\ncategory id >>> ")
        inp = input("number (default : all of them) >>> ")
        mn(url + gngbng[int(ct)], inp)

    if options.populare:
        st_num = input("\nnumber (default : all of them) >>> ")
        mn("https://bartarinha.com/favorites", st_num)

    if options.new:
        sth_num = input("\nnumber (default : all of them) >>> ")
        mn("https://bartarinha.com/newests?page=1", sth_num)
    if options.manual != "":
        sth_nu = input("\nnumber (default : all of them) >>> ")
        mn(options.manual, sth_nu)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_agent()
        main()
    else:
        par.print_help()
    if sth_ls:
        checking(sth_ls)
