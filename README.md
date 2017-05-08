# How To Use 
# ikuass_API
ikuass bus

### Requirements
```shell=
pip install requests
```

### Run
```shell=
python bus_api.py
```

### Example

**Input**

Enter your student ID and password.

```
Enter Your Account:1104137125
Enter Your Password:
```
**Output**

預約成功


# bus_tool.py

## Class ikuasbus(date)
### Synopsis
```
import bus_tool

bus = bus_tool.ikuasbus('2017/05/08') # 查詢日期 'yyyy/mm/dd'
print (bus.get_busid(0)) #拿到第1筆 busid
print (bus.get_busid(1)) #拿到第2筆 busid
```
### get_busid(n)
  
  拿到第n筆busid

### get_driveTime(n)

   拿到第n筆開車時間
   
### get_startStation(n)

  拿到第n筆發車點

### get_endStation(n)

 拿到第n筆目的地

### get_specialBus(n)

 拿到是否為特殊班次 0 為否 1 為是
  
### get_specialMsg(n)

  拿到第n筆的備註
   
### get_resCount(n)

拿到第n筆的預約人數

### get_limitCount(n)

 拿到第n筆人數限制

###  get_resEnable(n)

拿到第n筆是否可預約

### get_resCode(n)


### get_resName(n)
 
拿到預約資訊

### get_datalen()

取得資料長度
