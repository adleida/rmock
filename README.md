# rmock


![rmock](https://github.com/adleida/adkit/raw/master/bid.png?raw=true)

### introduction
rmock 模拟DSP bid server

### install

```bash
$ git clone https://github.com/adleida/rmock.git
$ cd rmock
$ sudo python3 setup.py install
```

### URL

- `/`
    > `method: GET`

    > intro: 获取rmock的运行状态信息

    > **response:**

    >```javascript
    {
        "Rmock": "Welcome to rmock dsp",
        "timestamp": 1434005808.0010495,
        "version": "0.0.6"
    }
    ```

- `/conf`
    > `method POST`

    > intro: config rmock运行状态

    > `post` 内容需要满足以下格式：

    >```javascript
"dsp": {
   "s": [
     {
       "id": "110",
       "name": "品友",
       "burl": "http://dsp:6001/res/v2/110",
       "res_file": {},
       "notice_file": {},
       "is_res": true
     }
   ],
   "tsleep": 5,
   "info": {
     "host": "0.0.0.0",
     "port": 6001
   }
 }
    ```

    > **response:**

    >```javascript
    {
        "conf": true
    }
    ```
- `/dsp/v2`
    > `method GET`

    > intro: 获取DSP列表

    > **response:**

    >```javascript
    [
      {
        "burl": "http://dsp:6001/res/v2/110",
        "name": "品友",
        "id": "110"
      }
    ]
    ```

- `/res/v2/<string:did>`

    > `method POST`

    > intro: bid url

    > **response:**

    >```javascript
    {'is_test': 0, 'adm': []}
    ```

    > **Note:** bid 成功后adm才会有值

- `/notice/v2/<string:did>`

    > `method POST`

    > intro: bid url

    > **response:**

    >```javascript
    {
        "message": "110 get notice",
        "time": 1434007891.3947947
    }
    ```
