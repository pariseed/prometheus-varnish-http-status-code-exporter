from prometheus_client import start_http_server, Gauge
import os
import re
import time

gauge100 = Gauge('HTTP_100_CODE', 'number of varnish http satus code')
regex100 = re.compile(".*(.00..100)")
counter100 = 0

gauge101 = Gauge('HTTP_101_CODE', 'number of varnish http satus code')
regex101 = re.compile(".*(.00..101)")
counter101 = 0

gauge102 = Gauge('HTTP_102_CODE', 'number of varnish http satus code')
regex102 = re.compile(".*(.00..102)")
counter102 = 0

gauge103 = Gauge('HTTP_103_CODE', 'number of varnish http satus code')
regex103 = re.compile(".*(.00..103)")
counter103 = 0

gauge200 = Gauge('HTTP_200_CODE', 'number of varnish http satus code')
regex200 = re.compile(".*(.00..200)")
counter200 = 0

gauge201 = Gauge('HTTP_201_CODE', 'number of varnish http satus code')
regex201 = re.compile(".*(.00..201)")
counter201 = 0

gauge202 = Gauge('HTTP_202_CODE', 'number of varnish http satus code')
regex202 = re.compile(".*(.00..202)")
counter202 = 0

gauge203 = Gauge('HTTP_203_CODE', 'number of varnish http satus code')
regex203 = re.compile(".*(.00..203)")
counter203 = 0

gauge204 = Gauge('HTTP_204_CODE', 'number of varnish http satus code')
regex204 = re.compile(".*(.00..204)")
counter204 = 0

gauge205 = Gauge('HTTP_205_CODE', 'number of varnish http satus code')
regex205 = re.compile(".*(.00..205)")
counter205 = 0

gauge206 = Gauge('HTTP_206_CODE', 'number of varnish http satus code')
regex206 = re.compile(".*(.00..206)")
counter206 = 0

gauge207 = Gauge('HTTP_207_CODE', 'number of varnish http satus code')
regex207 = re.compile(".*(.00..207)")
counter207 = 0

gauge208 = Gauge('HTTP_208_CODE', 'number of varnish http satus code')
regex208 = re.compile(".*(.00..208)")
counter208 = 0

gauge226 = Gauge('HTTP_226_CODE', 'number of varnish http satus code')
regex226 = re.compile(".*(.00..226)")
counter226 = 0

gauge300 = Gauge('HTTP_300_CODE', 'number of varnish http satus code')
regex300 = re.compile(".*(.00..300)")
counter300 = 0

gauge301 = Gauge('HTTP_301_CODE', 'number of varnish http satus code')
regex301 = re.compile(".*(.00..301)")
counter301 = 0

gauge302 = Gauge('HTTP_302_CODE', 'number of varnish http satus code')
regex302 = re.compile(".*(.00..302)")
counter302 = 0

gauge303 = Gauge('HTTP_303_CODE', 'number of varnish http satus code')
regex303 = re.compile(".*(.00..303)")
counter303 = 0

gauge304 = Gauge('HTTP_304_CODE', 'number of varnish http satus code')
regex304 = re.compile(".*(.00..304)")
counter304 = 0

gauge305 = Gauge('HTTP_305_CODE', 'number of varnish http satus code')
regex305 = re.compile(".*(.00..305)")
counter305 = 0

gauge306 = Gauge('HTTP_306_CODE', 'number of varnish http satus code')
regex306 = re.compile(".*(.00..306)")
counter306 = 0

gauge307 = Gauge('HTTP_307_CODE', 'number of varnish http satus code')
regex307 = re.compile(".*(.00..307)")
counter307 = 0

gauge308 = Gauge('HTTP_308_CODE', 'number of varnish http satus code')
regex308 = re.compile(".*(.00..308)")
counter308 = 0

gauge400 = Gauge('HTTP_400_CODE', 'number of varnish http satus code')
regex400 = re.compile(".*(.00..400)")
counter400 = 0

gauge401 = Gauge('HTTP_401_CODE', 'number of varnish http satus code')
regex401 = re.compile(".*(.00..401)")
counter401 = 0

gauge402 = Gauge('HTTP_402_CODE', 'number of varnish http satus code')
regex402 = re.compile(".*(.00..402)")
counter402 = 0

gauge403 = Gauge('HTTP_403_CODE', 'number of varnish http satus code')
regex403 = re.compile(".*(.00..403)")
counter403 = 0

gauge404 = Gauge('HTTP_404_CODE', 'number of varnish http satus code')
regex404 = re.compile(".*(.00..404)")
counter404 = 0

gauge405 = Gauge('HTTP_405_CODE', 'number of varnish http satus code')
regex405 = re.compile(".*(.00..405)")
counter405 = 0

gauge406 = Gauge('HTTP_406_CODE', 'number of varnish http satus code')
regex406 = re.compile(".*(.00..406)")
counter406 = 0

gauge407 = Gauge('HTTP_407_CODE', 'number of varnish http satus code')
regex407 = re.compile(".*(.00..407)")
counter407 = 0

gauge408 = Gauge('HTTP_408_CODE', 'number of varnish http satus code')
regex408 = re.compile(".*(.00..408)")
counter408 = 0

gauge409 = Gauge('HTTP_409_CODE', 'number of varnish http satus code')
regex409 = re.compile(".*(.00..409)")
counter409 = 0

gauge410 = Gauge('HTTP_410_CODE', 'number of varnish http satus code')
regex410 = re.compile(".*(.00..410)")
counter410 = 0

gauge411 = Gauge('HTTP_411_CODE', 'number of varnish http satus code')
regex411 = re.compile(".*(.00..411)")
counter411 = 0

gauge412 = Gauge('HTTP_412_CODE', 'number of varnish http satus code')
regex412 = re.compile(".*(.00..412)")
counter412 = 0

gauge413 = Gauge('HTTP_413_CODE', 'number of varnish http satus code')
regex413 = re.compile(".*(.00..413)")
counter413 = 0

gauge414 = Gauge('HTTP_414_CODE', 'number of varnish http satus code')
regex414 = re.compile(".*(.00..414)")
counter414 = 0

gauge415 = Gauge('HTTP_415_CODE', 'number of varnish http satus code')
regex415 = re.compile(".*(.00..415)")
counter415 = 0

gauge416 = Gauge('HTTP_416_CODE', 'number of varnish http satus code')
regex416 = re.compile(".*(.00..416)")
counter416 = 0

gauge417 = Gauge('HTTP_417_CODE', 'number of varnish http satus code')
regex417 = re.compile(".*(.00..417)")
counter417 = 0

gauge418 = Gauge('HTTP_418_CODE', 'number of varnish http satus code')
regex418 = re.compile(".*(.00..418)")
counter418 = 0

gauge421 = Gauge('HTTP_421_CODE', 'number of varnish http satus code')
regex421 = re.compile(".*(.00..421)")
counter421 = 0

gauge422 = Gauge('HTTP_422_CODE', 'number of varnish http satus code')
regex422 = re.compile(".*(.00..422)")
counter422 = 0

gauge423 = Gauge('HTTP_423_CODE', 'number of varnish http satus code')
regex423 = re.compile(".*(.00..423)")
counter423 = 0

gauge424 = Gauge('HTTP_424_CODE', 'number of varnish http satus code')
regex424 = re.compile(".*(.00..424)")
counter424 = 0

gauge425 = Gauge('HTTP_425_CODE', 'number of varnish http satus code')
regex425 = re.compile(".*(.00..425)")
counter425 = 0

gauge426 = Gauge('HTTP_426_CODE', 'number of varnish http satus code')
regex426 = re.compile(".*(.00..426)")
counter426 = 0

gauge427 = Gauge('HTTP_427_CODE', 'number of varnish http satus code')
regex427 = re.compile(".*(.00..427)")
counter427 = 0

gauge428 = Gauge('HTTP_428_CODE', 'number of varnish http satus code')
regex428 = re.compile(".*(.00..428)")
counter428 = 0

gauge429 = Gauge('HTTP_429_CODE', 'number of varnish http satus code')
regex429 = re.compile(".*(.00..429)")
counter429 = 0

gauge431 = Gauge('HTTP_431_CODE', 'number of varnish http satus code')
regex431 = re.compile(".*(.00..431)")
counter431 = 0

gauge451 = Gauge('HTTP_451_CODE', 'number of varnish http satus code')
regex451 = re.compile(".*(.00..451)")
counter451 = 0

gauge500 = Gauge('HTTP_500_CODE', 'number of varnish http satus code')
regex500 = re.compile(".*(.00..500)")
counter500 = 0

gauge501 = Gauge('HTTP_501_CODE', 'number of varnish http satus code')
regex501 = re.compile(".*(.00..501)")
counter501 = 0

gauge502 = Gauge('HTTP_502_CODE', 'number of varnish http satus code')
regex502 = re.compile(".*(.00..502)")
counter502 = 0

gauge503 = Gauge('HTTP_503_CODE', 'number of varnish http satus code')
regex503 = re.compile(".*(.00..503)")
counter503 = 0

gauge504 = Gauge('HTTP_504_CODE', 'number of varnish http satus code')
regex504 = re.compile(".*(.00..504)")
counter504 = 0

gauge505 = Gauge('HTTP_505_CODE', 'number of varnish http satus code')
regex505 = re.compile(".*(.00..505)")
counter505 = 0

gauge506 = Gauge('HTTP_506_CODE', 'number of varnish http satus code')
regex506 = re.compile(".*(.00..506)")
counter506 = 0

gauge507 = Gauge('HTTP_507_CODE', 'number of varnish http satus code')
regex507 = re.compile(".*(.00..507)")
counter507 = 0

gauge508 = Gauge('HTTP_508_CODE', 'number of varnish http satus code')
regex508 = re.compile(".*(.00..508)")
counter508 = 0

gauge510 = Gauge('HTTP_510_CODE', 'number of varnish http satus code')
regex510 = re.compile(".*(.00..510)")
counter510 = 0

gauge511 = Gauge('HTTP_511_CODE', 'number of varnish http satus code')
regex511 = re.compile(".*(.00..511)")
counter511 = 0

gauge700 = Gauge('HTTP_700_CODE', 'number of varnish http satus code')
regex700 = re.compile(".*(.00..700)")
counter700 = 0



def http100():
        for elem in codestat :
                if regex100.match(elem):
			global counter100 
                        r = elem.split('100')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
				floo = float(k)
                        except ValueError:
				break
			sult = abs(floo-counter100) 
			if counter100 == 0:
                                sult = 0.0
			gauge100.set(sult)
			counter100 = floo			


def http101():
        for elem in codestat :
                if regex101.match(elem):
			global counter101
                        r = elem.split('101')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter101)
			if counter101 == 0:
                                sult = 0.0
                        gauge101.set(sult)
                        counter101 = floo




def http102():
        for elem in codestat :
                if regex102.match(elem):
			global counter102
                        r = elem.split('102')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter102)
			if counter102 == 0:
                                sult = 0.0
                        gauge102.set(sult)
                        counter102 = floo
			


def http103():
        for elem in codestat :
                if regex103.match(elem):
			global counter103
                        r = elem.split('103')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter103)
			if counter103 == 0:
                                sult = 0.0
                        gauge103.set(sult)
                        counter103 = floo





def http200():
	for elem in codestat :
        	if regex200.match(elem):
			global counter200
                	r = elem.split('200')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter200)
			if counter200 == 0:
                                sult = 0.0
                        gauge200.set(sult)
                        counter200 = floo
			



def http201():
        for elem in codestat :
                if regex201.match(elem):
			global counter201
                        r = elem.split('201')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter201)
			if counter201 == 0:
                                sult = 0.0
                        gauge201.set(sult)
                        counter201 = floo




def http202():
        for elem in codestat :
                if regex202.match(elem):
			global counter202
                        r = elem.split('202')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter202)
			if counter202 == 0:
                                sult = 0.0
                        gauge202.set(sult)
                        counter202 = floo




def http203():
        for elem in codestat :
                if regex203.match(elem):
			global counter203
                        r = elem.split('203')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter203)
			if counter203 == 0:
                                sult = 0.0
                        gauge203.set(sult)
                        counter203 = floo
		



def http204():
        for elem in codestat :
                if regex204.match(elem):
			global counter204
                        r = elem.split('204')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter204)
			if counter204 == 0:
                                sult = 0.0
                        gauge204.set(sult)
                        counter204 = floo





def http205():
        for elem in codestat :
                if regex205.match(elem):
			global counter205
                        r = elem.split('205')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter205)
			if counter205 == 0:
                                sult = 0.0
                        gauge205.set(sult)
                        counter205 = floo




def http206():
        for elem in codestat :
                if regex206.match(elem):
			global counter206
                        r = elem.split('206')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter206)
			if counter206 == 0:
                                sult = 0.0
                        gauge206.set(sult)
                        counter206 = floo





def http207():
        for elem in codestat :
                if regex207.match(elem):
			global counter207
                        r = elem.split('207')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter207)
			if counter207 == 0:
                                sult = 0.0
                        gauge207.set(sult)
                        counter207 = floo
		



def http208():
        for elem in codestat :
                if regex208.match(elem):
			global counter208
                        r = elem.split('208')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter208)
			if counter208 == 0:
                                sult = 0.0
                        gauge208.set(sult)
                        counter208 = floo




def http226():
        for elem in codestat :
                if regex226.match(elem):
			global counter226
                        r = elem.split('226')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter226)
			if counter226 == 0:
                                sult = 0.0
                        gauge226.set(sult)
                        counter226 = floo	




def http300():
        for elem in codestat :
                if regex300.match(elem):
			global counter300
                        r = elem.split('300')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter300)
			if counter300 == 0:
                                sult = 0.0
                        gauge300.set(sult)
                        counter300 = floo





def http301():
        for elem in codestat :
                if regex301.match(elem):
			global counter301
                        r = elem.split('301')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter301)
			if counter301 == 0:
                                sult = 0.0
                        gauge301.set(sult)
                        counter301 = floo





def http302():
        for elem in codestat :
                if regex302.match(elem):
			global counter302
                        r = elem.split('302')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter302)
			if counter302 == 0:
                                sult = 0.0
                        gauge302.set(sult)
                        counter302 = floo




def http303():
        for elem in codestat :
                if regex303.match(elem):
			global counter303
                        r = elem.split('303')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter303)
			if counter303 == 0:
                                sult = 0.0
                        gauge303.set(sult)
                        counter303 = floo




def http304():
        for elem in codestat :
                if regex304.match(elem):
			global counter304
                        r = elem.split('304')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter304)
			if counter304 == 0:
                                sult = 0.0
                        gauge304.set(sult)
                        counter304 = floo





def http305():
        for elem in codestat :
                if regex305.match(elem):
			global counter305
                        r = elem.split('305')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter305)
			if counter305 == 0:
                                sult = 0.0
                        gauge305.set(sult)
                        counter305 = floo





def http306():
        for elem in codestat :
                if regex306.match(elem):
			global counter306
                        r = elem.split('306')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter306)
			if counter306 == 0:
                                sult = 0.0
                        gauge306.set(sult)
                        counter306 = floo





def http307():
        for elem in codestat :
                if regex307.match(elem):
			global counter307
                        r = elem.split('307')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
                        sult = abs(floo-counter307)
			if counter307 == 0:
                                sult = 0.0
                        gauge307.set(sult)
                        counter307 = floo






def http308():
        for elem in codestat :
                if regex308.match(elem):
			global counter308
                        r = elem.split('308')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter308)
			if counter308 == 0:
                                sult = 0.0
                        gauge308.set(sult)
                        counter308 = floo





def http400():
        for elem in codestat :
                if regex400.match(elem):
			global counter400
                        r = elem.split('400')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter400)
			if counter400 == 0:
                                sult = 0.0
                        gauge400.set(sult)
                        counter400 = floo





def http401():
        for elem in codestat :
                if regex401.match(elem):
			global counter401
                        r = elem.split('401')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter401)
			if counter401 == 0:
                                sult = 0.0
                        gauge401.set(sult)
                        counter401 = floo






def http402():
        for elem in codestat :
                if regex402.match(elem):
			global counter402
                        r = elem.split('402')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter402)
			if counter402 == 0:
                                sult = 0.0
                        gauge402.set(sult)
                        counter402 = floo





def http403():
        for elem in codestat :
                if regex403.match(elem):
			global counter403
                        r = elem.split('403')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter403)
			if counter403 == 0:
                                sult = 0.0
                        gauge403.set(sult)
                        counter403 = floo





def http404():
        for elem in codestat :
                if regex404.match(elem):
			global counter404
                        r = elem.split('404')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter404)
			if counter404 == 0:
                                sult = 0.0
                        gauge404.set(sult)
                        counter404 = floo





def http405():
        for elem in codestat :
                if regex405.match(elem):
			global counter405
                        r = elem.split('405')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter405)
			if counter405 == 0:
                                sult = 0.0
                        gauge405.set(sult)
                        counter405 = floo






def http406():
        for elem in codestat :
                if regex406.match(elem):
			global counter406
                        r = elem.split('406')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter406)
			if counter406 == 0:
                                sult = 0.0
                        gauge406.set(sult)
                        counter406 = floo





def http407():
        for elem in codestat :
                if regex407.match(elem):
			global counter407
                        r = elem.split('407')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter407)
			if counter407 == 0:
                                sult = 0.0
                        gauge407.set(sult)
                        counter407 = floo




def http408():
        for elem in codestat :
                if regex408.match(elem):
			global counter408
                        r = elem.split('408')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter408)
			if counter408 == 0:
                                sult = 0.0
                        gauge408.set(sult)
                        counter408 = floo




def http409():
        for elem in codestat :
                if regex409.match(elem):
			global counter409
                        r = elem.split('409')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter409)
			if counter409 == 0:
                                sult = 0.0
                        gauge409.set(sult)
                        counter409 = floo





def http410():
        for elem in codestat :
                if regex410.match(elem):
			global counter410
                        r = elem.split('410')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter410)
			if counter410 == 0:
                                sult = 0.0
                        gauge410.set(sult)
                        counter410 = floo





def http411():
        for elem in codestat :
                if regex411.match(elem):
			global counter411
                        r = elem.split('411')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter411)
			if counter411 == 0:
                                sult = 0.0
                        gauge411.set(sult)
                        counter411 = floo






def http412():
        for elem in codestat :
                if regex412.match(elem):
			global counter412
                        r = elem.split('412')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter412)
			if counter412 == 0:
                                sult = 0.0
                        gauge412.set(sult)
                        counter412 = floo




def http413():
        for elem in codestat :
                if regex413.match(elem):
			global counter413
                        r = elem.split('413')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter413)
			if counter413 == 0:
                                sult = 0.0
                        gauge413.set(sult)
                        counter413 = floo




def http414():
        for elem in codestat :
                if regex414.match(elem):
			global counter414
                        r = elem.split('414')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter414)
			if counter414 == 0:
                                sult = 0.0
                        gauge414.set(sult)
                        counter414 = floo





def http415():
        for elem in codestat :
                if regex415.match(elem):
			global counter415
                        r = elem.split('415')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter415)
			if counter415 == 0:
                                sult = 0.0
                        gauge415.set(sult)
                        counter415 = floo





def http416():
        for elem in codestat :
                if regex416.match(elem):
			global counter416
                        r = elem.split('416')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter416)
			if counter416 == 0:
                                sult = 0.0
                        gauge416.set(sult)
                        counter416 = floo





def http417():
        for elem in codestat :
                if regex417.match(elem):
			global counter417
                        r = elem.split('417')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter417)
			if counter417 == 0:
                                sult = 0.0
                        gauge417.set(sult)
                        counter417 = floo





def http418():
        for elem in codestat :
                if regex418.match(elem):
			global counter418
                        r = elem.split('418')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter418)
			if counter418 == 0:
                                sult = 0.0
                        gauge418.set(sult)
                        counter418 = floo




def http421():
        for elem in codestat :
                if regex421.match(elem):
			global counter421
                        r = elem.split('421')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter421)
			if counter421 == 0:
                                sult = 0.0
                        gauge421.set(sult)
                        counter421 = floo





def http422():
        for elem in codestat :
                if regex422.match(elem):
			global counter422
                        r = elem.split('422')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter422)
			if counter422 == 0:
                                sult = 0.0
                        gauge422.set(sult)
                        counter422 = floo






def http423():
        for elem in codestat :
                if regex423.match(elem):
			global counter423
                        r = elem.split('423')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter423)
			if counter423 == 0:
                                sult = 0.0
                        gauge423.set(sult)
                        counter423 = floo






def http424():
        for elem in codestat :
                if regex424.match(elem):
			global counter424
                        r = elem.split('424')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter424)
			if counter424 == 0:
                                sult = 0.0
                        gauge424.set(sult)
                        counter424 = floo







def http425():
        for elem in codestat :
                if regex425.match(elem):
			global counter425
                        r = elem.split('425')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter425)
			if counter425 == 0:
                                sult = 0.0
                        gauge425.set(sult)
                        counter425 = floo






def http426():
        for elem in codestat :
                if regex426.match(elem):
			global counter426
                        r = elem.split('426')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter426)
			if counter426 == 0:
                                sult = 0.0
                        gauge426.set(sult)
                        counter426 = floo





def http427():
        for elem in codestat :
                if regex427.match(elem):
			global counter427
                        r = elem.split('427')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter427)
			if counter427 == 0:
                                sult = 0.0
                        gauge427.set(sult)
                        counter427 = floo





def http428():
        for elem in codestat :
                if regex428.match(elem):
			global counter428
                        r = elem.split('428')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter428)
			if counter428 == 0:
                                sult = 0.0
                        gauge428.set(sult)
                        counter428 = floo







def http429():
        for elem in codestat :
                if regex429.match(elem):
			global counter429
                        r = elem.split('429')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter429)
			if counter429 == 0:
                                sult = 0.0
                        gauge429.set(sult)
                        counter429 = floo






def http431():
        for elem in codestat :
                if regex431.match(elem):
			global counter431
                        r = elem.split('431')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter431)
			if counter431 == 0:
                                sult = 0.0
                        gauge431.set(sult)
                        counter431 = floo






def http451():
        for elem in codestat :
                if regex451.match(elem):
			global counter451
                        r = elem.split('451')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter451)
			if counter451 == 0:
                                sult = 0.0
                        gauge451.set(sult)
                        counter451 = floo







def http500():
        for elem in codestat :
                if regex500.match(elem):
			global counter500
                        r = elem.split('500')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter500)
			if counter500 == 0:
                                sult = 0.0
                        gauge500.set(sult)
                        counter500 = floo






def http501():
        for elem in codestat :
                if regex501.match(elem):
			global counter501
                        r = elem.split('501')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter501)
			if counter501 == 0:
                                sult = 0.0
                        gauge501.set(sult)
                        counter501 = floo






def http502():
        for elem in codestat :
                if regex502.match(elem):
			global counter502
                        r = elem.split('502')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter502)
			if counter502 == 0:
                                sult = 0.0
                        gauge502.set(sult)
                        counter502 = floo







def http503():
        for elem in codestat :
                if regex503.match(elem):
			global counter503
                        r = elem.split('503')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter503)
			if counter503 == 0:
                                sult = 0.0
                        gauge503.set(sult)
                        counter503 = floo





def http504():
        for elem in codestat :
                if regex504.match(elem):
			global counter504
                        r = elem.split('504')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter504)
			if counter504 == 0:
                                sult = 0.0
                        gauge504.set(sult)
                        counter504 = floo






def http505():
        for elem in codestat :
                if regex505.match(elem):
			global counter505
                        r = elem.split('505')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter505)
			if counter505 == 0:
                                sult = 0.0
                        gauge505.set(sult)
                        counter505 = floo






def http506():
        for elem in codestat :
                if regex506.match(elem):
			global counter506
                        r = elem.split('506')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter506)
			if counter506 == 0:
                                sult = 0.0
                        gauge506.set(sult)
                        counter506 = floo







def http507():
        for elem in codestat :
                if regex507.match(elem):
			global counter507
                        r = elem.split('507')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter507)
			if counter507 == 0:
                                sult = 0.0
                        gauge507.set(sult)
                        counter507 = floo






def http508():
        for elem in codestat :
                if regex508.match(elem):
			global counter508
                        r = elem.split('508')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter508)
			if counter508 == 0:
                                sult = 0.0
                        gauge508.set(sult)
                        counter508 = floo

			





def http510():
        for elem in codestat :
                if regex510.match(elem):
			global counter510
                        r = elem.split('510')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter510)
			if counter510 == 0:
                                sult = 0.0
                        gauge510.set(sult)
                        counter510 = floo







def http511():
        for elem in codestat :
                if regex511.match(elem):
			global counter511
                        r = elem.split('511')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter511)
			if counter511 == 0:
                                sult = 0.0
                        gauge511.set(sult)
                        counter511 = floo







def http700():
        for elem in codestat :
                if regex700.match(elem):
			global counter700
                        r = elem.split('700')
                        res = "('%s')" % "','".join(r)
                        regg = "\('|',''\)"
                        k = re.sub(regg, '', res)
			try:
                                floo = float(k)
                        except ValueError:
                                break
			sult = abs(floo-counter700)
			if counter700 == 0:
                                sult = 0.0
                        gauge700.set(sult)
                        counter700 = floo





def start():

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




if __name__ == '__main__':


        start_http_server(8002)
	
	while True:
		httpcode = os.popen("varnishtop -1 | grep RespStatus | sed 's/\<RespStatus\>//g'").read()
                codestat =  httpcode.splitlines()

		start()
		time.sleep(1)
