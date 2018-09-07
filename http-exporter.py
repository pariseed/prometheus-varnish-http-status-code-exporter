// Copyright 2018 Daniele Parise
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.






from prometheus_client import start_http_server, Gauge
import os
import re
import time

gauge100 = Gauge('HTTP_100_CODE', 'number of varnish http satus code')
regex100 = re.compile(".*(.00..100)")

gauge101 = Gauge('HTTP_101_CODE', 'number of varnish http satus code')
regex101 = re.compile(".*(.00..101)")

gauge102 = Gauge('HTTP_102_CODE', 'number of varnish http satus code')
regex102 = re.compile(".*(.00..102)")

gauge103 = Gauge('HTTP_103_CODE', 'number of varnish http satus code')
regex103 = re.compile(".*(.00..103)")

gauge200 = Gauge('HTTP_200_CODE', 'number of varnish http satus code')
regex200 = re.compile(".*(.00..200)")

gauge201 = Gauge('HTTP_201_CODE', 'number of varnish http satus code')
regex201 = re.compile(".*(.00..201)")

gauge202 = Gauge('HTTP_202_CODE', 'number of varnish http satus code')
regex202 = re.compile(".*(.00..202)")

gauge203 = Gauge('HTTP_203_CODE', 'number of varnish http satus code')
regex203 = re.compile(".*(.00..203)")

gauge204 = Gauge('HTTP_204_CODE', 'number of varnish http satus code')
regex204 = re.compile(".*(.00..204)")

gauge205 = Gauge('HTTP_205_CODE', 'number of varnish http satus code')
regex205 = re.compile(".*(.00..205)")

gauge206 = Gauge('HTTP_206_CODE', 'number of varnish http satus code')
regex206 = re.compile(".*(.00..206)")

gauge207 = Gauge('HTTP_207_CODE', 'number of varnish http satus code')
regex207 = re.compile(".*(.00..207)")

gauge208 = Gauge('HTTP_208_CODE', 'number of varnish http satus code')
regex208 = re.compile(".*(.00..208)")

gauge226 = Gauge('HTTP_226_CODE', 'number of varnish http satus code')
regex226 = re.compile(".*(.00..226)")

gauge300 = Gauge('HTTP_300_CODE', 'number of varnish http satus code')
regex300 = re.compile(".*(.00..300)")

gauge301 = Gauge('HTTP_301_CODE', 'number of varnish http satus code')
regex301 = re.compile(".*(.00..301)")

gauge302 = Gauge('HTTP_302_CODE', 'number of varnish http satus code')
regex302 = re.compile(".*(.00..302)")

gauge303 = Gauge('HTTP_303_CODE', 'number of varnish http satus code')
regex303 = re.compile(".*(.00..303)")

gauge304 = Gauge('HTTP_304_CODE', 'number of varnish http satus code')
regex304 = re.compile(".*(.00..304)")

gauge305 = Gauge('HTTP_305_CODE', 'number of varnish http satus code')
regex305 = re.compile(".*(.00..305)")

gauge306 = Gauge('HTTP_306_CODE', 'number of varnish http satus code')
regex306 = re.compile(".*(.00..306)")

gauge307 = Gauge('HTTP_307_CODE', 'number of varnish http satus code')
regex307 = re.compile(".*(.00..307)")

gauge308 = Gauge('HTTP_308_CODE', 'number of varnish http satus code')
regex308 = re.compile(".*(.00..308)")

gauge400 = Gauge('HTTP_400_CODE', 'number of varnish http satus code')
regex400 = re.compile(".*(.00..400)")

gauge401 = Gauge('HTTP_401_CODE', 'number of varnish http satus code')
regex401 = re.compile(".*(.00..401)")

gauge402 = Gauge('HTTP_402_CODE', 'number of varnish http satus code')
regex402 = re.compile(".*(.00..402)")

gauge403 = Gauge('HTTP_403_CODE', 'number of varnish http satus code')
regex403 = re.compile(".*(.00..403)")

gauge404 = Gauge('HTTP_404_CODE', 'number of varnish http satus code')
regex404 = re.compile(".*(.00..404)")

gauge405 = Gauge('HTTP_405_CODE', 'number of varnish http satus code')
regex405 = re.compile(".*(.00..405)")

gauge406 = Gauge('HTTP_406_CODE', 'number of varnish http satus code')
regex406 = re.compile(".*(.00..406)")

gauge407 = Gauge('HTTP_407_CODE', 'number of varnish http satus code')
regex407 = re.compile(".*(.00..407)")

gauge408 = Gauge('HTTP_408_CODE', 'number of varnish http satus code')
regex408 = re.compile(".*(.00..408)")

gauge409 = Gauge('HTTP_409_CODE', 'number of varnish http satus code')
regex409 = re.compile(".*(.00..409)")

gauge410 = Gauge('HTTP_410_CODE', 'number of varnish http satus code')
regex410 = re.compile(".*(.00..410)")

gauge411 = Gauge('HTTP_411_CODE', 'number of varnish http satus code')
regex411 = re.compile(".*(.00..411)")

gauge412 = Gauge('HTTP_412_CODE', 'number of varnish http satus code')
regex412 = re.compile(".*(.00..412)")

gauge413 = Gauge('HTTP_413_CODE', 'number of varnish http satus code')
regex413 = re.compile(".*(.00..413)")

gauge414 = Gauge('HTTP_414_CODE', 'number of varnish http satus code')
regex414 = re.compile(".*(.00..414)")

gauge415 = Gauge('HTTP_415_CODE', 'number of varnish http satus code')
regex415 = re.compile(".*(.00..415)")

gauge416 = Gauge('HTTP_416_CODE', 'number of varnish http satus code')
regex416 = re.compile(".*(.00..416)")

gauge417 = Gauge('HTTP_417_CODE', 'number of varnish http satus code')
regex417 = re.compile(".*(.00..417)")

gauge418 = Gauge('HTTP_418_CODE', 'number of varnish http satus code')
regex418 = re.compile(".*(.00..418)")

gauge421 = Gauge('HTTP_421_CODE', 'number of varnish http satus code')
regex421 = re.compile(".*(.00..421)")

gauge422 = Gauge('HTTP_422_CODE', 'number of varnish http satus code')
regex422 = re.compile(".*(.00..422)")

gauge423 = Gauge('HTTP_423_CODE', 'number of varnish http satus code')
regex423 = re.compile(".*(.00..423)")

gauge424 = Gauge('HTTP_424_CODE', 'number of varnish http satus code')
regex424 = re.compile(".*(.00..424)")

gauge425 = Gauge('HTTP_425_CODE', 'number of varnish http satus code')
regex425 = re.compile(".*(.00..425)")

gauge426 = Gauge('HTTP_426_CODE', 'number of varnish http satus code')
regex426 = re.compile(".*(.00..426)")

gauge427 = Gauge('HTTP_427_CODE', 'number of varnish http satus code')
regex427 = re.compile(".*(.00..427)")

gauge428 = Gauge('HTTP_428_CODE', 'number of varnish http satus code')
regex428 = re.compile(".*(.00..428)")

gauge429 = Gauge('HTTP_429_CODE', 'number of varnish http satus code')
regex429 = re.compile(".*(.00..429)")

gauge431 = Gauge('HTTP_431_CODE', 'number of varnish http satus code')
regex431 = re.compile(".*(.00..431)")

gauge451 = Gauge('HTTP_451_CODE', 'number of varnish http satus code')
regex451 = re.compile(".*(.00..451)")

gauge500 = Gauge('HTTP_500_CODE', 'number of varnish http satus code')
regex500 = re.compile(".*(.00..500)")

gauge501 = Gauge('HTTP_501_CODE', 'number of varnish http satus code')
regex501 = re.compile(".*(.00..501)")

gauge502 = Gauge('HTTP_502_CODE', 'number of varnish http satus code')
regex502 = re.compile(".*(.00..502)")

gauge503 = Gauge('HTTP_503_CODE', 'number of varnish http satus code')
regex503 = re.compile(".*(.00..503)")

gauge504 = Gauge('HTTP_504_CODE', 'number of varnish http satus code')
regex504 = re.compile(".*(.00..504)")

gauge505 = Gauge('HTTP_505_CODE', 'number of varnish http satus code')
regex505 = re.compile(".*(.00..505)")

gauge506 = Gauge('HTTP_506_CODE', 'number of varnish http satus code')
regex506 = re.compile(".*(.00..506)")

gauge507 = Gauge('HTTP_507_CODE', 'number of varnish http satus code')
regex507 = re.compile(".*(.00..507)")

gauge508 = Gauge('HTTP_508_CODE', 'number of varnish http satus code')
regex508 = re.compile(".*(.00..508)")

gauge510 = Gauge('HTTP_510_CODE', 'number of varnish http satus code')
regex510 = re.compile(".*(.00..510)")

gauge511 = Gauge('HTTP_511_CODE', 'number of varnish http satus code')
regex511 = re.compile(".*(.00..511)")


gauge700 = Gauge('HTTP_700_CODE', 'number of varnish http satus code')
regex700 = re.compile(".*(.00..700)")




def http100():
        for elem in codestat :
                if regex100.match(elem):
                        r = elem.split('100')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
				floo = float(k)
                        except ValueError:
				break
                        gauge100.set(floo)


def http101():
        for elem in codestat :
                if regex101.match(elem):
                        r = elem.split('101')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge101.set(floo)




def http102():
        for elem in codestat :
                if regex102.match(elem):
                        r = elem.split('102')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge102.set(floo)


def http103():
        for elem in codestat :
                if regex103.match(elem):
                        r = elem.split('103')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge103.set(floo)





def http200():
	for elem in codestat :
        	if regex200.match(elem):
                	r = elem.split('200')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge200.set(floo)



def http201():
        for elem in codestat :
                if regex201.match(elem):
                        r = elem.split('201')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge201.set(floo)




def http202():
        for elem in codestat :
                if regex202.match(elem):
                        r = elem.split('202')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge202.set(floo)




def http203():
        for elem in codestat :
                if regex203.match(elem):
                        r = elem.split('203')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge203.set(floo)



def http204():
        for elem in codestat :
                if regex204.match(elem):
                        r = elem.split('204')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge204.set(floo)



def http205():
        for elem in codestat :
                if regex205.match(elem):
                        r = elem.split('205')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge205.set(floo)




def http206():
        for elem in codestat :
                if regex206.match(elem):
                        r = elem.split('206')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge206.set(floo)



def http207():
        for elem in codestat :
                if regex207.match(elem):
                        r = elem.split('207')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge207.set(floo)



def http208():
        for elem in codestat :
                if regex208.match(elem):
                        r = elem.split('208')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge208.set(floo)



def http226():
        for elem in codestat :
                if regex226.match(elem):
                        r = elem.split('226')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge226.set(floo)
	


def http300():
        for elem in codestat :
                if regex300.match(elem):
                        r = elem.split('300')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge300.set(floo)



def http301():
        for elem in codestat :
                if regex301.match(elem):
                        r = elem.split('301')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge301.set(floo)




def http302():
        for elem in codestat :
                if regex302.match(elem):
                        r = elem.split('302')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge302.set(floo)



def http303():
        for elem in codestat :
                if regex303.match(elem):
                        r = elem.split('303')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge303.set(floo)



def http304():
        for elem in codestat :
                if regex304.match(elem):
                        r = elem.split('304')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge304.set(floo)



def http305():
        for elem in codestat :
                if regex305.match(elem):
                        r = elem.split('305')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge305.set(floo)




def http306():
        for elem in codestat :
                if regex306.match(elem):
                        r = elem.split('306')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge306.set(floo)




def http307():
        for elem in codestat :
                if regex307.match(elem):
                        r = elem.split('307')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge307.set(floo)




def http308():
        for elem in codestat :
                if regex308.match(elem):
                        r = elem.split('308')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge308.set(floo)




def http400():
        for elem in codestat :
                if regex400.match(elem):
                        r = elem.split('400')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge400.set(floo)




def http401():
        for elem in codestat :
                if regex401.match(elem):
                        r = elem.split('401')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge401.set(floo)





def http402():
        for elem in codestat :
                if regex402.match(elem):
                        r = elem.split('402')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge402.set(floo)




def http403():
        for elem in codestat :
                if regex403.match(elem):
                        r = elem.split('403')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge403.set(floo)



def http404():
        for elem in codestat :
                if regex404.match(elem):
                        r = elem.split('404')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge404.set(floo)



def http405():
        for elem in codestat :
                if regex405.match(elem):
                        r = elem.split('405')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge405.set(floo)



def http406():
        for elem in codestat :
                if regex406.match(elem):
                        r = elem.split('406')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge406.set(floo)



def http407():
        for elem in codestat :
                if regex407.match(elem):
                        r = elem.split('407')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge407.set(floo)



def http408():
        for elem in codestat :
                if regex408.match(elem):
                        r = elem.split('408')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge408.set(floo)



def http409():
        for elem in codestat :
                if regex409.match(elem):
                        r = elem.split('409')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge409.set(floo)



def http410():
        for elem in codestat :
                if regex410.match(elem):
                        r = elem.split('410')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge410.set(floo)



def http411():
        for elem in codestat :
                if regex411.match(elem):
                        r = elem.split('411')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge411.set(floo)



def http412():
        for elem in codestat :
                if regex412.match(elem):
                        r = elem.split('412')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge412.set(floo)



def http413():
        for elem in codestat :
                if regex413.match(elem):
                        r = elem.split('413')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge413.set(floo)



def http414():
        for elem in codestat :
                if regex414.match(elem):
                        r = elem.split('414')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge414.set(floo)




def http415():
        for elem in codestat :
                if regex415.match(elem):
                        r = elem.split('415')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge415.set(floo)



def http416():
        for elem in codestat :
                if regex416.match(elem):
                        r = elem.split('416')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge416.set(floo)




def http417():
        for elem in codestat :
                if regex417.match(elem):
                        r = elem.split('417')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge417.set(floo)	



def http418():
        for elem in codestat :
                if regex418.match(elem):
                        r = elem.split('418')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge418.set(floo)




def http421():
        for elem in codestat :
                if regex421.match(elem):
                        r = elem.split('421')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge421.set(floo)




def http422():
        for elem in codestat :
                if regex422.match(elem):
                        r = elem.split('422')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge422.set(floo)




def http423():
        for elem in codestat :
                if regex423.match(elem):
                        r = elem.split('423')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge423.set(floo)




def http424():
        for elem in codestat :
                if regex424.match(elem):
                        r = elem.split('424')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge424.set(floo)





def http425():
        for elem in codestat :
                if regex425.match(elem):
                        r = elem.split('425')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge425.set(floo)





def http426():
        for elem in codestat :
                if regex426.match(elem):
                        r = elem.split('426')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge426.set(floo)




def http427():
        for elem in codestat :
                if regex427.match(elem):
                        r = elem.split('427')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge427.set(floo)




def http428():
        for elem in codestat :
                if regex428.match(elem):
                        r = elem.split('428')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge428.set(floo)




def http429():
        for elem in codestat :
                if regex429.match(elem):
                        r = elem.split('429')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge429.set(floo)




def http431():
        for elem in codestat :
                if regex431.match(elem):
                        r = elem.split('431')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge431.set(floo)	




def http451():
        for elem in codestat :
                if regex451.match(elem):
                        r = elem.split('451')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge451.set(floo)




def http500():
        for elem in codestat :
                if regex500.match(elem):
                        r = elem.split('500')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge500.set(floo)




def http501():
        for elem in codestat :
                if regex501.match(elem):
                        r = elem.split('501')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge501.set(floo)




def http502():
        for elem in codestat :
                if regex502.match(elem):
                        r = elem.split('502')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge502.set(floo)




def http503():
        for elem in codestat :
                if regex503.match(elem):
                        r = elem.split('503')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge503.set(floo)




def http504():
        for elem in codestat :
                if regex504.match(elem):
                        r = elem.split('504')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge504.set(floo)





def http505():
        for elem in codestat :
                if regex505.match(elem):
                        r = elem.split('505')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge505.set(floo)




def http506():
        for elem in codestat :
                if regex506.match(elem):
                        r = elem.split('506')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge506.set(floo)



def http507():
        for elem in codestat :
                if regex507.match(elem):
                        r = elem.split('507')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge507.set(floo)



def http508():
        for elem in codestat :
                if regex508.match(elem):
                        r = elem.split('508')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge508.set(floo)




def http510():
        for elem in codestat :
                if regex510.match(elem):
                        r = elem.split('510')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge510.set(floo)




def http511():
        for elem in codestat :
                if regex511.match(elem):
                        r = elem.split('511')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge511.set(floo)





def http700():
        for elem in codestat :
                if regex700.match(elem):
                        r = elem.split('700')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        gauge700.set(floo)





if __name__ == '__main__':


        start_http_server(8002)
	
	while True:
		httpcode = os.popen("varnishtop -1 | grep RespStatus | sed 's/\<RespStatus\>//g'").read()
                codestat =  httpcode.splitlines()

		http100()
		http101()
		http102()
		http103()
		http200()
		http201()
		http202()
		http203()
		http204()
		http205()
		http206()
		http207()
		http208()
		http226()
		http300()
		http301()
		http302()
		http303()
		http304()
		http305()
		http306()
		http307()
		http308()
		http400()
		http401()
		http402()
		http403()
		http404()
		http405()
		http406()
		http407()
		http408()
		http409()
		http410()
		http411()
		http412()
		http413()
		http414()
		http415()
		http416()
		http417()
		http418()
		http421()
		http422()
		http423()
		http424()
		http425()
		http426()
		http427()
		http428()
		http429()
		http431()
		http451()
		http500()
		http501()
		http502()
		http503()
		http504()
		http505()
		http506()
		http507()
		http508()
		http510()
		http511()
		http700()
		time.sleep(10)
