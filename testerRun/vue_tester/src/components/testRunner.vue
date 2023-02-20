<template>

 <html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Gooxi Test Platform</title>
    <!-- 引入 css文件 -->
<!--      <link rel="stylesheet" type="text/css" href= "{{ url_for('static', filename = 'css/bootstrap-4.4.1.css') }}">-->
  </head>
  <body onload="startClock()" onunload="stopClock()">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <img src="src/assets/gooxi2.jpg" alt="" class="img-fluid" style="position:absolute;top:0;left:0">
        <form class="form-inline my-2 my-lg-0" method="post" action="/submitForSearch">
          <h1 class="text-center" style="color: white;margin-left: 930px">Gooxi Test Platform v1.0</h1>
        </form>
      </div>
    </nav>


	  <div class="divFor5rec">
          <div class="hangLeft"><h3 style="background-color: #008000;color: white">前测试区</h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3 style="background-color: #000000;color: white">扫码区域</h3></div>
          <div class="hangLeft"><h3>SN号 : </h3></div>
          <div class="shuangzi"><a class="snNumber" href="#" id="snNumber" role="button">               </a></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
		  <div class="hangLeft"><h3>工号 : </h3></div>
          <div class="bmc_ip_font"><a class="bmc_ip" href="#" id="bmc_ip" role="button">                </a></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3 style="background-color: #FFA500" onclick="showGreen()"> 上一站 </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3 style="background-color: #FFA500" onclick="showYellow()"> 下一站 </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
		  <div class="hangLeft"><h3 style="background-color: #FFA500" onclick="showRed()"> 老  化 </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>时间</h3></div>
          <div class="shuangzi"><a class="runningTime" id="runningTime" href="#" role="button"></a><div class="showTime"></div></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3>            </h3></div>
          <div class="hangLeft"><h3 style="background-color: #008000;color: white">复测试区</h3></div>


      </div>

    <hr>

    <hr>
	<hr>

    <hr>
    <div class="container">
        <div class="container py-sm-4">
          <div class="row">
			<hr>
			 <div class="laohuajiankong">
			 </div>
			  <br>

             <div class="blockFor9_1" style="border-bottom: 5px solid black; border-left: 5px solid black;border-right: 5px solid black;border-top: 5px solid black">
                 <div class="show-info">
                  <h3 style="text-align: center">信息显示区</h3>>
                  <h4>
                    FRU Device Description : Builtin FRU Device (ID 0)<br>
                     Board Mfg Date        : Tue Aug  9 00:00:00 2022<br>
                     Board Mfg             : GOOXI<br>
                     Board Product         : G3DCL-B<br>
                     Board Serial          : 220528080715017501<br>
                     Board Part Number     : 1.21.222.0346<br>
                     Product Manufacturer  : GOOXI<br>
                     Product Part Number   : 0.11.004.0038<br>
                     Product Serial        : 2207220034S22072700038
                  </h4>
                </div>
                 <div class="show-standard">
                  <h3 style="text-align: center">标准参数显示区</h3>>
                  <h4>
                    CPUnumber : 2<br>
                    Architecture: loongarch64<br>
                    CPU(s): 32<br>
                    MEM: 64G<br>
                    FAN: 16<br>
                    DISK: 128G
                  </h4>
                </div>
            </div>
              <div class="blockFor9_2" style="border-bottom: 5px solid black; border-left: 5px solid black;border-right: 5px solid black;border-top: 5px solid black">
                <div class="show-compare">
                  <h3 style="text-align: center">对比结果显示区</h3>>
                  <h4 style="color: #1e7e34">
                    BIOS_FW: B;<br>
                    BMC_FW : GX00015;<br>
                    CPUnumber : PASS;<br>
                    CPU(s) :2207220034S22072700038;<br>
                    MEMtotal: :220811135124;<br>
                    MEMnumber:f8:f0:82:35:1c:81 f8:f0:82:35:1c:82;<br>
                    BIOS : PASS ;<br>
                    Disk total number(硬盘数量): PASS;<br>
                    fannumber: PASS;<br>
                    Board Mfg: PASS;<br>
                    Board Product: PASS;<br>
                    Board Serial:PASS;<br>
                    Ethernet Count: PASS;
                  </h4>
                </div>
              </div>
              <div class="blockFor9_2" style="border-bottom: 5px solid black; border-left: 5px solid black;border-right: 5px solid black;border-top: 5px solid black">
                  <div class="show-test-form">
                      <h3 style="color: #004085;text-align: center">测试表显示区</h3>
                  </div>
                  <div class="show-test-form">
                        <h4 style="color: #004085;text-align: center">
                        CPU<br>
                        MEM<br>
                        FAN<br>
                        HDD<br>
                        PCIE<br>
                        BIOS<br>
                        Disk<br>
                        FRU<br>
                        SDD<br>
                        USB<br>
                        ID灯
                      </h4>
                  </div>
                </div>

          </div>
          <div class="row">

             <div class="blockFor9_1" style="border-bottom: 5px solid black; border-left: 5px solid black;border-right: 5px solid black;border-top: 5px solid black">
              <div class="show-info">
                  <h3 class="startTest" style="background-color: #34ce57;text-align: center">开始测试</h3>
              </div>
            </div>
              <div class="blockFor9_2" style="border-bottom: 5px solid black; border-left: 5px solid black;border-right: 5px solid black;border-top: 5px solid black">
                  <div class="show-compare">
                      <h3 class="stopTest" style="background-color: #c82333;text-align: center">停止测试</h3>
                  </div>
              </div>
              <div class="blockFor9_2" style="border-bottom: 5px solid black; border-left: 5px solid black;border-right: 5px solid black;border-top: 5px solid black">
                  <div class="show-test-form">
                      <h3 class="uploadLog" style="background-color: #9fcdff;text-align: center">日志上传</h3>
                  </div>
              </div>

          </div>


              <br>

          </div>



			<div class="divForHelp">
			   	  <div class="textForHelp"><a class="buttonOfHelp btn" href="#" onclick="repeat()">操作帮助</a></div>
			</div>

                  </div>


    <footer class="text-center">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <p>版权所有 © 2023 深圳市国鑫恒运信息安全有限公司 保留一切权利</p>
          </div>
        </div>
      </div>
    </footer>

  </body>
</html>


</template>


    <script>
        let flag1=0;
        let flag2=0;
        let flag3=0;
        var timer = null;
        var date=new Date();
        var d1=date.toLocaleString();
        var buttonElements=document.querySelectorAll('.eachButton');
        //set their IDs
        for(var i=0;i<buttonElements.length;i++)
        {
            buttonElements[i].id='eachButton-'+i;
            buttonElements[i].innerHTML=buttonElements[i].name;
        }

    export default {
      name: "testRunner",
      methods: {
        startTest () {
          // 开始测试逻辑
        },
        stopTest () {
          // 停止测试逻辑
        },
        showTestItems () {
            this.axios.get('show_testItems/')
            .then((response) => {
                console.log(response.data.list);
                this.tableData = response.data.list
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        time(){
          var t = null;
            t = setTimeout(time, 1000);   //原本置于time()之外

            clearTimeout(t);
            var showTime = document.querySelector('.showTime');
            var date = new Date();
            const year=date.getFullYear();
            var month=date.getMonth()+1;
            const dates=date.getDate();
            if(month<10)
                month="0"+month;
            if(date<10)
                date="0"+date;
            var times=year + "-" + month + "-" + dates;
            const hour = date.getHours();
            const minutes = date.getMinutes();
            const seconds = date.getSeconds();
            showTime.innerHTML = `${times} ${hour} : ${minutes} : ${seconds}`;
            t = setTimeout(time, 1000);
        },
        displayClock(num){
            if (num < 10) {
               return "0" + num;
           } else {
               return num;
           }
        },
        stopClock(){
          clearTimeout(timer);
        },
        startClock(){
         var time = new Date();
         var hours = displayClock(time.getHours()) + ":";
         var minutes = displayClock(time.getMinutes()) + ":";
         var seconds = displayClock(time.getSeconds());
         //显示时间
         for (var i = 0; i < 108; i++) {
             document.getElementById("eachButton-" + i.toString()).style.background = window.list[i];

             if (window.list[i] == "#dc3545" || window.list[i] == "#fff" || window.list[i] == "#00FFFF" || window.list[i] == "#0000FF") {
                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name+ "\n" +"00:00:00";//在id为show的块区域显示
             }
             else if (window.list[i] == "#28a745") {
                 let sysTime=new Date();
                 var createTime=new Date(timeTotalList[i][0]);
                 let hh=Math.round(parseInt(sysTime-createTime)/1000/60/60%24);
                 let mm=Math.round(parseInt(sysTime-createTime)/1000/60%60);
                 let ss=Math.round(parseInt(sysTime-createTime)/1000%60);
                 let hhh=displayClock(hh + ":");
                 let mmm=displayClock(mm + ":");
                 let sss=displayClock(ss);
                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name + "\n" + hhh + mmm + sss;//在id为show的块区域显示
             }
             else if (window.list[i] == "#FFA500" || window.list[i] == "#FFFF00") {

                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name + "\n" + window.timeTotalList[i][3];
             }
             else if (window.list[i] == "#800080") {

                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name + "\n" + window.timeTotalList[i][3];

             }
             else {
                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name;//在id为show的块区域显示
             }
         }
         timer = setTimeout("startClock()", 1000);//延时器
        },
      }
    }
    </script>

<style scoped>

</style>
