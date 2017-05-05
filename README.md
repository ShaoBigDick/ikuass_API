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
### Requirements
```shell=
pip install requests
```
**Input**

get_bus_list('yyyy/mm/dd')

**Output**

{"success":true,"message":"","count":23,"data":[{"busId":33824,"driveTime":"06:50","startStation":"建工","endStation":"燕巢","specialBus":"0","specialMsg":"","resCount":47,"limitCount":999,"resEnable":false,"resCode":"","resName":"不可預約"},{"busId":33914,"driveTime":"07:20","startStation":"建工","endStation":"燕巢","specialBus":"0","specialMsg":"","resCount":103,"limitCount":999,"resEnable":false,"resCode":"","resName":"不可預約"}
......
