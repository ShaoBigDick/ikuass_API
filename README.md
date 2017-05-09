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
#### get_busid(index)
  
  取得busid

#### get_driveTime(index)

  取得開車時間
   
#### get_startStation(index)

  取得發車點

#### get_endStation(index)

  取得目的地

#### get_specialBus(index)

 取得特殊班次 0 為否 1 為是
  
#### get_specialMsg(index)

 取得備註
   
#### get_resCount(index)

 取得目前預約人數

#### get_limitCount(index)

 取得人數限制

####  get_resEnable(index)

 取得是否可預約 (True or Flase)

#### get_resCode(index)


#### get_resName(index)
 
取得預約資訊

#### get_datalen()

取得資料長度


## Class ikuaslogin(userId,userPw)
### Synopsis



