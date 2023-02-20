
<!--&lt;!&ndash;            <script>&ndash;&gt;-->
<!--&lt;!&ndash;          $.ajax({&ndash;&gt;-->
<!--&lt;!&ndash;                 async:false,&ndash;&gt;-->
<!--&lt;!&ndash;                 type: "POST",&ndash;&gt;-->
<!--&lt;!&ndash;                 url: "/get_timeList",&ndash;&gt;-->
<!--&lt;!&ndash;                 success: function (timeTotalList) {&ndash;&gt;-->
<!--&lt;!&ndash;                     window.timeTotalList = timeTotalList;&ndash;&gt;-->
<!--&lt;!&ndash;                 },&ndash;&gt;-->
<!--&lt;!&ndash;                     error: function () {&ndash;&gt;-->
<!--&lt;!&ndash;                         console.log();&ndash;&gt;-->
<!--&lt;!&ndash;                         {&ndash;&gt;-->
<!--&lt;!&ndash;                             alert("time list ajax error!!!!!!!!!!!!!!!!");&ndash;&gt;-->
<!--&lt;!&ndash;                         }&ndash;&gt;-->
<!--&lt;!&ndash;                     }&ndash;&gt;-->
<!--&lt;!&ndash;                 })&ndash;&gt;-->
<!--&lt;!&ndash;              </script>&ndash;&gt;-->


<!--            <script>-->
<!--                     var timer = null;-->

<!--                     function displayClock(num) {//num是传入的startClock中的动态值-->
<!--                         if (num < 10) {-->
<!--                             return "0" + num;-->
<!--                         } else {-->
<!--                             return num;-->
<!--                         }-->
<!--                     }-->

<!--                     //停止计时-->
<!--                     function stopClock() {-->
<!--                         clearTimeout(timer);-->
<!--                     }-->

<!--                     //开始计时-->
<!--                     function startClock() {-->
<!--                         var time = new Date();-->
<!--                         var hours = displayClock(time.getHours()) + ":";-->
<!--                         var minutes = displayClock(time.getMinutes()) + ":";-->
<!--                         var seconds = displayClock(time.getSeconds());-->
<!--                         //显示时间-->
<!--                         for (var i = 0; i < 108; i++) {-->
<!--                             document.getElementById("eachButton-" + i.toString()).style.background = window.list[i];-->

<!--                             if (window.list[i] == "#dc3545" || window.list[i] == "#fff" || window.list[i] == "#00FFFF" || window.list[i] == "#0000FF") {-->
<!--                                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name+ "\n" +"00:00:00";//在id为show的块区域显示-->
<!--                             }-->
<!--                             else if (window.list[i] == "#28a745") {-->
<!--                                 let sysTime=new Date();-->
<!--                                 var createTime=new Date(timeTotalList[i][0]);-->
<!--                                 hh=Math.round(parseInt(sysTime-createTime)/1000/60/60%24);-->
<!--                                 mm=Math.round(parseInt(sysTime-createTime)/1000/60%60);-->
<!--                                 ss=Math.round(parseInt(sysTime-createTime)/1000%60);-->
<!--                                 hhh=displayClock(hh + ":");-->
<!--                                 mmm=displayClock(mm + ":");-->
<!--                                 sss=displayClock(ss);-->
<!--                                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name + "\n" + hhh + mmm + sss;//在id为show的块区域显示-->
<!--                             }-->
<!--                             else if (window.list[i] == "#FFA500" || window.list[i] == "#FFFF00") {-->

<!--                                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name + "\n" + window.timeTotalList[i][3];-->
<!--                             }-->
<!--                             else if (window.list[i] == "#800080") {-->

<!--                                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name + "\n" + window.timeTotalList[i][3];-->

<!--                             }-->
<!--                             else {-->
<!--                                 document.getElementById("eachButton-" + i).innerHTML = document.getElementById("eachButton-" + i).name;//在id为show的块区域显示-->
<!--                             }-->
<!--                         }-->
<!--                         timer = setTimeout("startClock()", 1000);//延时器-->
<!--                     }-->

<!--            </script>-->

<!--            <script>-->
<!--                let flag1=0;-->
<!--                let flag2=0;-->
<!--                let flag3=0;-->
<!--            </script>-->


<!--            {# 功能：显示按钮颜色#}-->
<!--            <script>-->
<!--                 $.ajax({-->
<!--                     async:false,-->
<!--                     type: "POST",-->
<!--                     url: "/get_status",-->
<!--                     success: function (statusList) {-->
<!--                         window.list=statusList;-->
<!--                         var totalMach=108;-->
<!--                         var runningMach=0;-->
<!--                         var finishedMach=0;-->
<!--                         var errorMach=0;-->
<!--                         var yellowMach=0;-->
<!--                         var green="#28a745";-->
<!--                         var red="#dc3545";-->
<!--                         var orange="#FFA500";-->
<!--                         var yellow="#FFFF00";-->
<!--                         var qing="#00FFFF";-->
<!--                         var blue="#0000FF";-->
<!--                         var purp="#800080";-->
<!--                         var white="#fff";-->
<!--                         for(eachStatus of statusList)-->
<!--                         {-->
<!--                             if(eachStatus==green) {-->
<!--                                 runningMach = runningMach + 1;-->
<!--                             }-->
<!--                             else if(eachStatus==red) {-->
<!--                                 errorMach = errorMach + 1;-->
<!--                             }-->
<!--                             else if(eachStatus==yellow) {-->
<!--                                 yellowMach = yellowMach + 1;-->
<!--                             }-->
<!--                             else-->
<!--                                 finishedMach=finishedMach+1;-->
<!--                         }-->
<!--                         document.getElementById("totalGreen").innerHTML=runningMach;-->
<!--                         document.getElementById("totalRed").innerHTML=errorMach;-->
<!--                         document.getElementById("totalYellow").innerHTML=yellowMach;-->
<!--                     },-->
<!--                     error: function () {-->
<!--                         console.log();-->
<!--                         {-->
<!--                             alert("error!!!!!!!!!!!!!!!!");-->
<!--                         }-->
<!--                     }-->
<!--                 })-->
<!--            </script>-->

<!--            {# 功能：为每个按钮添加点击事件#}-->
<!--            <script>-->
<!--                function f1(a)-->
<!--                {-->
<!--                    $.ajax({-->
<!--                     url: "/sendButtonRack",-->
<!--                     contentType: "POST",-->
<!--                     data:{"rack":a},-->
<!--                     success: function (dict) {-->
<!--                         document.getElementById("bmc_ip").innerHTML=dict[0];-->
<!--                         document.getElementById("tester").innerHTML=dict[4];-->
<!--                         document.getElementById("snNumber").innerHTML=dict[5];-->
<!--                         if(document.getElementById("btnForSSH")){-->
<!--                             var deleteButton=document.getElementById("btnForSSH");-->
<!--                             console.log("deleteButton found!");-->
<!--                             console.log(deleteButton.id);-->
<!--                             document.body.removeChild(deleteButton);-->
<!--                         }else {-->
<!--                             console.log("deleteButton not found!");-->
<!--                         }-->
<!--                         if(document.getElementById("btnForBMC")){-->
<!--                             var deleteButton2=document.getElementById("btnForBMC");-->
<!--                             console.log("deleteButton2 found!");-->
<!--                             console.log(deleteButton2.id);-->
<!--                             document.body.removeChild(deleteButton2);-->
<!--                         }else {-->
<!--                             console.log("deleteButton2 not found!");-->
<!--                         }-->
<!--                         var sshBtn = document.createElement("input");-->
<!--                         var bmcBtn = document.createElement("input");-->
<!--                         sshBtn.id = "btnForSSH";-->
<!--                         sshBtn.class="childButton";-->
<!--                         sshBtn.type = "button";-->
<!--                         sshBtn.value = "进入"+a.substring(8,13)+"终端";-->
<!--                         sshBtn.style.cssText = "width:120px; height:50px;background:#D98719;position:absolute;top:150px;left:900px";-->
<!--                         bmcBtn.id = "btnForBMC";-->
<!--                         bmcBtn.class="childButton";-->
<!--                         bmcBtn.type = "button";-->
<!--                         bmcBtn.value = a.substring(8,13)+"跳转BMC";-->
<!--                         bmcBtn.style.cssText = "width:120px; height:50px;background:#00FFFF;position:absolute;top:150px;left:1100px";-->
<!--                         var IPP=dict[6];-->
<!--                         var BMCIP=dict[7];-->
<!--                         sshBtn.onclick=function(){-->
<!--                             console.log("http://127.0.0.1:8888/?hostname="+IPP+"&username=root&password=MQ==&port=22");-->
<!--                             window.open("http://127.0.0.1:8888/?hostname="+IPP+"&username=root&password=MQ==&port=22")-->
<!--                         };-->
<!--                         bmcBtn.onclick=function(){-->
<!--                             console.log("https://"+BMCIP+"/#login");-->
<!--                             window.open("https://"+BMCIP+"/#login&username=admin&password=admin&port=433");-->
<!--                         };-->

<!--                         document.body.appendChild(sshBtn);-->
<!--                         document.body.appendChild(bmcBtn);-->
<!--                     },-->
<!--                     error: function () {-->
<!--                         console.log();-->
<!--                         {-->
<!--                             alert("button click function error!!!!!!!!!!!!!!!!");-->
<!--                         }-->
<!--                     }-->
<!--                 })-->
<!--                }-->
<!--            </script>-->

<!--            <script>-->
<!--                function showGreen()-->
<!--                {-->
<!--                    $.ajax({-->
<!--                     async:false,-->
<!--                     type: "POST",-->
<!--                     url: "/showGreen",-->
<!--                     success: function (totalStatusList) {-->
<!--                         console.log("totalStatusList总状态列表的值为：")-->
<!--                         console.log(totalStatusList);-->
<!--                         if(flag1==0)-->
<!--                         {-->
<!--                             for(eachStatusList of totalStatusList)-->
<!--                             {-->
<!--                                 if(eachStatusList[1]!=3)-->
<!--                                 {-->
<!--                                    console.log("不为绿的状态值为：");-->
<!--                                    console.log(eachStatusList[1]);-->
<!--                                    console.log("不为绿的老化架号为：");-->
<!--                                    console.log(eachStatusList[0]);-->
<!--                                    console.log("document.getElementsByClassName为(eachStatusList[0])：");-->
<!--                                    selector=document.getElementsByName(eachStatusList[0]);-->
<!--                                    element=$(selector);-->
<!--                                    element.hide();-->
<!--                                 }-->
<!--                                 else-->
<!--                                 {-->
<!--                                    selector=document.getElementsByName(eachStatusList[0]);-->
<!--                                    element=$(selector);-->
<!--                                    element.backgroundColor="#28a745";-->
<!--                                 }-->
<!--                             }-->
<!--                             flag1=1;-->
<!--                         }else-->
<!--                         {-->
<!--                             console.log("进入到切换的二函数");-->
<!--                             location.reload();-->
<!--                             flag1=0;-->
<!--                         }-->

<!--                     },-->
<!--                     error: function () {-->
<!--                         console.log();-->
<!--                         {-->
<!--                             alert("show and hidden color buttons error!!!!!!!!!!!!!!!!");-->
<!--                         }-->
<!--                     }-->
<!--                 })-->
<!--                }-->
<!--            </script>-->

<!--            <script>-->
<!--                function showYellow()-->
<!--                {-->
<!--                    $.ajax({-->
<!--                     async:false,-->
<!--                     type: "POST",-->
<!--                     url: "/showYellow",-->
<!--                     success: function (totalStatusList) {-->
<!--                         console.log("totalStatusList总状态列表的值为：")-->
<!--                         console.log(totalStatusList);-->
<!--                         if(flag2==0)-->
<!--                         {-->
<!--                             for(eachStatusList of totalStatusList)-->
<!--                             {-->
<!--                                 if(eachStatusList[1]!=2)-->
<!--                                 {-->
<!--                                    console.log("不为黄的状态值为：");-->
<!--                                    console.log(eachStatusList[1]);-->
<!--                                    console.log("不为黄的老化架号为：");-->
<!--                                    console.log(eachStatusList[0]);-->
<!--                                    console.log("document.getElementsByClassName为(eachStatusList[0])：");-->
<!--                                    selector=document.getElementsByName(eachStatusList[0]);-->
<!--                                    element=$(selector);-->
<!--                                    element.hide();-->
<!--                                 }-->
<!--                                 else-->
<!--                                 {-->
<!--                                    selector=document.getElementsByName(eachStatusList[0]);-->
<!--                                    element=$(selector);-->
<!--                                    element.backgroundColor="#FFFF00";-->
<!--                                 }-->
<!--                             }-->
<!--                             flag2=1;-->
<!--                         }-->
<!--                         else {-->

<!--                             console.log("进入到切换的二函数");-->
<!--                             location.reload();-->
<!--                             flag2=0;-->
<!--                         }-->

<!--                     },-->
<!--                     error: function () {-->
<!--                         console.log();-->
<!--                         {-->
<!--                             alert("show and hidden color buttons error!!!!!!!!!!!!!!!!");-->
<!--                         }-->
<!--                     }-->
<!--                 })-->
<!--                }-->
<!--            </script>-->

<!--            <script>-->
<!--                function showRed()-->
<!--                {-->
<!--                    $.ajax({-->
<!--                     async:false,-->
<!--                     type: "POST",-->
<!--                     url: "/showRed",-->
<!--                     success: function (totalStatusList) {-->
<!--                         console.log("totalStatusList总状态列表的值为：");-->
<!--                         console.log(totalStatusList);-->
<!--                         if(flag3==0)-->
<!--                         {-->
<!--                             for(eachStatusList of totalStatusList)-->
<!--                             {-->
<!--                                 if(eachStatusList[1]!=0)-->
<!--                                 {-->
<!--                                    console.log("不为红的状态值为：");-->
<!--                                    console.log(eachStatusList[1]);-->
<!--                                    console.log("不为红的老化架号为：");-->
<!--                                    console.log(eachStatusList[0]);-->
<!--                                    console.log("document.getElementsByClassName为(eachStatusList[0])：");-->
<!--                                    selector=document.getElementsByName(eachStatusList[0]);-->
<!--                                    element=$(selector);-->
<!--                                    element.hide();-->
<!--                                 }else-->
<!--                                 {-->
<!--                                    selector=document.getElementsByName(eachStatusList[0]);-->
<!--                                    element=$(selector);-->
<!--                                    element.backgroundColor="#dc3545";-->
<!--                                 }-->
<!--                             }-->
<!--                             flag3=1;-->
<!--                         }-->
<!--                         else-->
<!--                         {-->

<!--                             console.log("进入到切换的二函数");-->
<!--                             location.reload();-->
<!--                             flag3=0;-->
<!--                         }-->

<!--                     },-->
<!--                     error: function () {-->
<!--                         console.log();-->
<!--                         {-->
<!--                             alert("show and hidden color buttons error!!!!!!!!!!!!!!!!");-->
<!--                         }-->
<!--                     }-->
<!--                 })-->
<!--                }-->
<!--            </script>-->

<!--    <script>-->
<!--    export default {-->
<!--      name: "testRunner",-->
<!--      methods: {-->
<!--        startTest () {-->
<!--          // 开始测试逻辑-->
<!--        },-->
<!--        stopTest () {-->
<!--          // 停止测试逻辑-->
<!--        }-->
<!--      }-->
<!--    }-->
<!--    </script>-->

















