`
# <span style="color:red">**You will never feel that you love to do so** </span>




# quick start








```


---------
someone
---------
i must face real myself



-----
someone
----------
use ppt as the pre studied materail may be a good method

--------
task
---------
1.data source
2.which problems need to be checked?



------
camera live push stream


---------
someone
---------
from some ponit ,i feel that there is all kinds of businees chance.i can rent my sichuan home 
in mingsu.i can build a website for my college





--------
flask deal with json
----------
https://scotch.io/bar-talk/processing-incoming-request-data-in-flask




---------
someone
---------
there is a company which use data-visual tool to build  task!
rethink-db


--------
someone
--------

try to write somethins tohtml file


--------

swift function
----------
http://fuckingclosuresyntax.com/



--------
ios how to hide  ios keyboard
----------------
https://stackoverflow.com/questions/24180954/how-to-hide-keyboard-in-swift-on-pressing-return-key








--------
cs method and function
--------
in oop language,method always was mentioned ,in funtion language
the function is always mentioned.


-------
ios problem
----------
//
//  ViewController.swift
//
//

import UIKit

class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet var myTextField : UITextField

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.

        self.myTextField.delegate = self;
    }

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        self.view.endEditing(true)
        return false
    }
}


there is many code ,i donot understand!!!!


-------
ios swiftjson
--------
http://sharingtechbits.com/use-swiftyjson-to-deal-with-json-data-in-swift/
https://stackoverflow.com/questions/8641557/how-to-set-uitextfield-height
https://stackoverflow.com/questions/1345561/how-to-create-a-multiline-uitextfield



-------
ios problem
----------
in ios ,? and ! is very  bad problem




--------
someone
----------
my view is that why i am always so hurry?

-------
ios how to get user input
----------
https://stackoverflow.com/questions/25859986/getting-info-from-uitextfield







--------
ios develop project
---------
1.how to run project in mac simulator
2.how to run app in physic device
3.how to create a project and configure the project
4.how to create a single view app
5.how to add imageview,button
6.how to connect view with code
7.how to add images to asserts
8.how to invoke images


233
---------
ios
---------
https://stackoverflow.com/questions/26600359/dismiss-keyboard-with-a-uitextview


--------
python django
------------
https://stackoverflow.com/questions/29780060/trying-to-parse-request-body-from-post-in-django
--------
python json
-----------
https://godjango.com/blog/working-with-json-and-django/


---------
swift
----------
https://stackoverflow.com/questions/8641557/how-to-set-uitextfield-height


---------
heroku mysql
-----------
https://stackoverflow.com/questions/9822313/remote-connect-to-cleardb-heroku-database


--------
heroku mysql
------------
https://stackoverflow.com/questions/36082472/heroku-and-cleardb-error
https://stackoverflow.com/questions/36082472/heroku-and-cleardb-error




--------
ios swift
----------
https://stackoverflow.com/questions/31982513/how-to-send-a-post-request-with-body-in-swift


-------
someone
--------
i can make a prefer list and recomend according somethings

----------
someone
----------
may be i need to redesign my page in my weahterapp use database or python model

--------
someone
--------
i try to understand knowledge with anoly(leibi),so happy



----------
someone
--------
from some point ,i have no tuoyanzheng,but when i am deal with complexity problem,i feel
so puzzeld! this leads me to feel very confused and diffculty!when i am deal complex things
,i will feel so confused!how to deal with these diffcult things?i think  we need a good foudation

-----------
html  how to reload a html page
-----------
https://stackoverflow.com/questions/4644027/how-to-automatically-reload-a-page-after-a-given-period-of-inactivity


---------
someone
---------
from recent experment,i have known, do a good things,u cannot do a thing very well at once,u
must persist it .besides.many things when u get ,it seems vague!!besides,the design work is 
very impot.may be ,in the last period.u may think these work u have done are not very important







-----------
machine learning
-----------
https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471



---------------
someone
-----------
i cannot adapt the long course in homework ,why,i guess that it
is caused by management




--------
someone
--------
if i have let more things getting things donw,i will get more things to done





----------
someone
---------
about lab,i only need to do things mrs li ask!!

----------
someone
--------
 i have find that  when i write something.i can understand mo deeper than  not doing so!

--------
printer
--------
deal with the bug of printer online and offline
https://www.youtube.com/watch?v=pDs52eozyVo

-------
fudan crawler
--------
https://www.zhihu.com/question/20287342
--------
sep20
---------
1. design and impletment python a crawl file
2.read the miniest demo of blockchain
https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a249b


---------
algorithm
-----------
https://news.ycombinator.com/item?id=12021476
----------
someone
---------
i always try to break the system ,it may be self-ego
it may have brought many disaster



--------
someone
---------
may it be,i need to rethink that  need i restart my taobao tech service?






--------
someone
---------
tabao block my businees,that sucks,i need torethink how can i make profit


---------
someone
--------
how to find problem?
---------
someone
--------
i believe the friendship of people is maintained by 
make use of ecah others and communicate with each other
---------
someone
---------
https://hackerbits.com/
-----------
mail
--------------
http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html

------------
get youtube playlist all url
------------
https://github.com/rg3/youtube-dl/issues/6945
--------
using flask to send mail
----------

#used to recevie from data
@app.route('/receive',methods = ['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        
        '''
        month=request.form['cbomoth']
        
        day=request.form['cbodate']
        hour=request.form['cbohours']
        
        year=request.form['cboyear']
       '''
        email = request.form['txtemail']
        name = request.form['txtname']
        birthday = request.form['txtdob']
        sex = request.form['txtsex']
        service = request.form['txttreatment']
        date1 = request.form['txtdate']
        #date = str(month)+'/'+str(day)+','+str(year)
        date ='i have no idea'
        phone = request.form['txtmobile']
        coutry = request.form['country']
    else:
        phone = 'user have no any info about phone' 
    msg = Message("New order", sender="qwe15986300@163.com", recipients=["seresbookings@gmail.com"])
    msg.body = "Hello seresbeauty\n"+"i want to give u  the fellowing info\n"+'The service time i want is: '+str(date1)+'\n'+'country is: '+str(coutry)+'\n'+'my name is: '+str(name)+'\n'+'my sex is: '+str(sex)+'\n'+'my phone is: '+str(phone)+'\n'+'email  is: '+str(email)+'\n'+'i need the service: '+str(service)+'\n'
    mail.send(msg)  
    return render_template('appointment.html')


--------
plan:write a app to get design images
----------

changstarFudan,



----------
someone
---------
i need to understand where is market or say what is the things i am pasionate?


-------
someone
-------
there is a illusion of finishment
----------
someone
---------
in fact ,i cannot understand where my interest is ???


----------
js startup cs drag 
-------------
https://shopify.github.io/draggable/
        
-----------
sending emmail

-------
sublime open remote server file
----------
https://stackoverflow.com/questions/37458814/how-to-open-remote-files-in-sublime-text-3

-------
ffmpeg in windows install and download
--------
http://www.wikihow.com/Install-FFmpeg-on-Windows

-------
convert a page to mark down  and add page


-------
python pdf tools
--------
https://pypi.python.org/pypi/pdftools/1.0.6
https://github.com/MrLeeh/pdftools
directly clone the repository ,u can slove the problem

------
python
-----------
hex ----decimial
s=0x23
a=int(a,16)

-------
html form control
----------
https://www.w3schools.com/css/tryit.asp?filename=trycss_forms


------
fortune sale
---------
http://nathanbarry.com/sales/


-------
game
--------
https://medium.com/the-philipendium/how-i-managed-to-design-the-most-successful-educational-computer-game-of-all-time-4626ea09e184

------
opensource
----------
https://github.com/Pterodactyl/Panel

```

---------
someone
--------
making someone happy may be a good businees

--------
someone
---------
i have a feeling i need a reading list



---------
someone
---------
i think  i need to set a period of  time to prepare a project
when the project is not  organized into small step



--------
habit
---------
1.always profit
2.freewritting
3.try different route
4.gtd
5.use flinch as the sign of forward



---------
someone
---------
there is  a great number of resource for all kinds of resource 
,now i believe that i lack passion for somethings.i believe 
cs field is so large.i can find somethings i like,in other hands ,i doubt that for i lack strong programming skill so that i can not build interest,i am so confused

-------
hn
-----------
https://news.ycombinator.com/item?id=13849430
https://news.ycombinator.com/item?id=14039135
https://news.ycombinator.com/item?id=12957371
-------
hn book
---------
https://news.ycombinator.com/item?id=14477851

--------
hn economy
-----------

vhttps://news.ycombinator.com/item?id=12556160


--------
hn side project
----------
https://news.ycombinator.com/item?id=14718089
https://news.ycombinator.com/item?id=12720636
https://news.ycombinator.com/item?id=12720636
https://news.ycombinator.com/item?id=14978631
https://news.ycombinator.com/item?id=12186587
https://news.ycombinator.com/item?id=12670731
https://news.ycombinator.com/item?id=12243611
https://news.ycombinator.com/item?id=10924977
https://news.ycombinator.com/item?id=3029771
--------
hn startup
----------
https://news.ycombinator.com/item?id=13326535
---------
hn book
--------
https://news.ycombinator.com/item?id=15155833
https://news.ycombinator.com/item?id=8716111
----------
hn startup
---------
https://news.ycombinator.com/item?id=13139638
https://news.ycombinator.com/item?id=13576236


---------
understand people
----------
how to win friends and influence people is understand people


---------
english
----------
all right 好吧


----------
How To Create Windows 10 Bootable USB (Real Easy Way

https://www.youtube.com/watch?v=iosA3Bn9RMI




------
opensource make map
---------
https://tilemill-project.github.io/tilemill/
---------
someone
----------
teacher li ask me to read self-philography!

------------
reforce learning
-------------
explore 
expect
fangcha
shoujian
lineral evaluate
今天晚上真的感觉到困难是什么，当你在一个参数上面不断调试可能人变得成熟的标志是从内心里认可任何事情的成败是由多个参数共同影响，将知识转化为产品本身就是一个很难的过程，更何况一个用户喜欢的产品


-----------
someone
--------
from some point,i feel that about my pain will be sloved from mental ,if have any trouble in living.







-----------
english develop
----------
hello everyone,is there anyone who can help me to develop my spoken english?i will help you in chinese


-----------
video stiching
---------------
https://www.youtube.com/watch?v=3in4e_yYOIA
https://github.com/lukeyeager/StitcHD
https://github.com/wieden-kennedy/video-stitch
https://www.youtube.com/watch?v=a5OK6bwke3I
https://www.youtube.com/watch?v=cJa0WSNRbT8
https://www.youtube.com/watch?v=n3CsQEC4Z3U
https://www.youtube.com/redirect?redir_token=tLxmuJC4gVnVIMUhYDDC1XEb7Et8MTUwNzU0ODk1MkAxNTA3NDYyNTUy&v=n3CsQEC4Z3U&q=http%3A%2F%2Fwww.pyimagesearch.com%2F2016%2F01%2F25%2Freal-time-panorama-and-image-stitching-with-opencv%2F&event=video_description
https://www.pyimagesearch.com/2016/01/25/real-time-panorama-and-image-stitching-with-opencv/
http://www.learnopencv.com/homography-examples-using-opencv-python-c/
http://dawinproject.blogspot.com/2014/01/multiple-images-panorama-stitching-with.html
http://study.marearts.com/2015/02/real-time-stitching-multi-video-to-one.html
https://www.youtube.com/watch?v=sj3cbPWlYeE
http://home.ifi.uio.no/paalh/publications/files/ism2013-bagadus.pdf

------------
someone
-----------
 i donot feel that i have more advance in producity 
 did i need a standard to value myself



----------
deep learning for computer vision with python
------------------------------






---------
someone
---------
i can look for a parter from youtube to help me in english spoken english
so i can help it in chinese.






-----------
someone
----------
my direction will be specify in the fellowing area
1.math
2.english
3.people and behavior  and phycology
4.startup
5.cs
6.economy

----------
someone
---------
care about 















------------




![](.png)
-------
mp4 and mp3 merge a ffmpeg
---------
https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg


!ffmpeg -i 1.mp4 -i 1.m4a -c copy 2.mp4






1.cherish your health
2.cherish time 
3.make friends with others
--------
ffmpeg using ffmpeg to cut video
Cutting the videos based on start and end time using ffmpeg
---------------
https://stackoverflow.com/questions/18444194/cutting-the-videos-based-on-start-and-end-time-using-ffmpeg
!ffmpeg -i 3.mp4 -ss 00:01:02 -t 00:01:44  -async 1 -c copy cut1.mp4
the middle time is gap

------
youtube-dl high quility
----------
https://askubuntu.com/questions/486297/how-to-select-video-quality-from-youtube-dl

-------
someone
--------
if u have any ideal.accroding to my lessons ,u should take note of it
or u will forget  it

-------
someone
-------
there is a fact ,when i meet a expert,i will lack confidence to show my understanding
of the things








-------
hawking and diable
--------
https://01.org/sites/default/files/documentation/acat_stephen_hawking_intro.mp4



---------
youtube-dl download mp4
------------
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' url


------
help the disable
--d--------
https://01.org/community

------
someone future
-----------
i undestand that i want to make use of tech to buld the palace or arm to protect
us to get profit safetly

--------
hn about essay 
---------

https://news.ycombinator.com/item?id=15406826



---------
someone software  market
-----------------

https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/



--------
someone
--------
i need to get experience from others who own successful experience !!!!
--------
someone
--------
i have find that i have 



---------
someone
-----------
i need some books to understand the people when they are poor and no fame how to get wealth?????

---------
economy
----------
the market have two product,one is competement,another is completment.
the first,for example,when beef price go up.the demand for chiken will go up
,the second,when the numbers of car goes up,the gas will go up.it is to say.when
complement price down,the another will go up


---------
someone
----------
in the past,i want to undertsnad economy ,math,cs,people,english to develop 
my ability.



----------
software and economy
------------
https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/






-------
startup
-------
i have find that china seem to have no these startups ,such as,source graph ,understand
what is the key problem of servicing for tech industry 
https://scitools.com/
https://rollbar.com/vs/?v=a


------
someone
-------
help someone who is disable may bring tiny profit
-------
ssh fail
--------
https://serverfault.com/questions/396303/cant-ssh-into-linux-server

------
for bug
---------
https://rollbar.com/
-------
centos6 config
-------
samba https://rbgeek.wordpress.com/2012/05/25/how-to-install-samba-server-on-centos-6/


-------
someone
-------
0.retink what is the things i wanted the most!!! 
1.use new method to service the lab program
2.explore the pursose of git 










-------
bitcoin
-------
https://news.ycombinator.com/item?id=13716386


------
source code read tool
--------
https://www.sourcetrail.com/
https://ubuntuforums.org/showthread.php?t=2010761

-----------
atom code fold
--------
https://discuss.atom.io/t/how-does-code-folding-work-in-atom/23713





-------
bitco
---------







---------
cs
---------
i find that i will get frustrated when i am install some software with many requirements



-------
all to mp3
---------
https://stackoverflow.com/questions/3255674/convert-audio-files-to-mp3-using-ffmpeg


-------
mp4 to mp3
---------
https://askubuntu.com/questions/84584/converting-mp4-to-mp3


-------
python movie.py
------
https://zulko.github.io/moviepy/index.html

-----
0704
----------
1.25 try to slove installation package
2.25 del with ffmpeg
3.25 try to give the link status

----
python crawler
---------
beautifulsoup may be the simple schema for crawler
https://www.youtube.com/watch?v=3xQTJi2tqgk

-------
countdown timer design
-------------
1.







----------
cs linux configure a static network
-----------
http://ask.xmodulo.com/configure-static-ip-address-centos7.html


---
webm  mkv to mp4
-------
https://stackoverflow.com/questions/18123376/webm-to-mp4-conversion-using-ffmpeg
https://askubuntu.com/questions/50433/how-to-convert-mkv-file-into-mp4-file-losslessly

--------
ios app
--------
used to build ios or andrios app in golang




----------
0630
---------
1.25 try to start my work
2.25 try to chnage the network
3.25 try to deal with encoder[1]
4.25 deal with encoder[2]
5.25 try to del with decoder
6.25 try to deal with encoder
---------
vlc and atom Player
--------
https://github.com/tyage/video-player


--------
0706
---------
1.try to develop a atom package
2.try to develop a atom package






-------
atom editor package
---------
https://www.youtube.com/watch?v=cFAzqvYoHJs&list=PLfAgUyVGvIM2w5x1-sQRboHpO8MIIY56Z









--------
0703
-------
1.25 start my work and deal with the work
2.15 10 min words
3.15 try to test ivp final
4.25 try to migrate with mr wang
5.25 try to modify smip group
6.25 try to migrate with wangyifan
7.25 try to mgirate with wangyifan and package
-------
vim for python
---------
https://github.com/tao12345666333/vim
-------
jeffery，chandler，wangfang：
  你们好，至今日我工作已经满一年，特别感谢王旺，在新技术的学习与钻研上给我提供了及时并且非常建设性的意见未来若是取得极大的成就中，一定是因为受了较好的影响，这一年因为各种各样的帮助我已经学到了许多东西，感谢jeffery对待工作严谨的态度
给我今后的工作带来了极大的影响，感谢王芳买的俯卧撑支架等运动器材。希望在未来的日子更加携手共进，先提出加薪要求，综合各方面的原因
去年已经打通构造和发布一个软件的全部知识链条,不断提高解决实际问题的能力，更加重要的是能动脑筋解决问题和学以致用的能力，本年度的期望薪资是8.8k,希望从该月开始执行(亦即上月工资为8.8k)如无异议,本年度的愿景是不断吸收和转化国际上先进的经验与技术成为caton内视频方面的专家和国内顶尖的python专家，吃透vpn和整套youtube-dl 开源技术，更加具有创造能力和更加成熟的学科知识背景，为了继续能给caton提供创造动力和贡献力量，希望未来大家能营造更加具有创新和孵化行业领军专家和无暴力沟通的环境，帮助创造更好的事业环境，也请大家帮助我获得更大的成就！
欢迎各位向我提供建设性的意见
请转发该邮件至有关人士/  

------
atom player  video
------------
https://atom.io/packages/videoplayer


--------
python
----------
Accessing the index in Python 'for' loops
https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops


-------
srt embed video
-----------
https://stackoverflow.com/questions/7240247/add-srt-subtitle-to-video-with-ffmpeg
https://stackoverflow.com/questions/8672809/use-ffmpeg-to-add-text-subtitles
Raj vs. Siri - The Big Bang Theory-OliVkzBLey4
!ffmpeg -i test.mp4 -vf subtitles=test.vtt out1.avi
-------
python crawler
---------
https://www.youtube.com/watch?v=3xQTJi2tqgk
what happen

--------
7.06
--------
1.25 try to 10minutes words







-----------
format conversion
---------------------
i can add servce to my taobao

----------
youtube-dl only download subtitle
-----------
https://github.com/rg3/youtube-dl/issues/11026






----
0628
---------
1.25 try to develop the countdown timer!
2.25 try to develop the countdown timer
3.25 TRY to develop the countdown timer! and 10 minutes words
4.25 test the countdown script and try to move the things to disk!
5.25 try to develop the countdown timer scripts
6.25 try to develop the countdown scripts
6.25 try to develop the work
--------
business
-----------
https://journal.standardnotes.org/starting-a-business-as-a-developer-in-2017-4f4a2a0b1922

-------
vlc play youtube
--------
https://www.vlchelp.com/play-youtube-videos-vlc-media-player/


![test](test.png)




--------
0718
-------
1.25 start my work











------
0717
-------
1.25  10 min words
2.25 try to start python paralle problem
3.25 try to develop the producity


--------
english
--------
Everything else should be charged at decent professional rates immediately
retes ===price
-------
python source code
--------
http://pgbovine.net/cpython-internals.htm
--------
real damn
---------
http://pgbovine.net/philip-guo-cv.pdf
----------
shell tool
----------
https://github.com/robbyrussell/oh-my-zsh

--------------
complete  cs science
--------------
https://github.com/jwasham/coding-interview-university
--------
cs
--------
i can youtube-dl to download all kinds of package

----------------------------------
linux system comand comandline tool
-------------------------------
https://github.com/jlevy/the-art-of-command-line

-------
developer reoadmap
---------
https://github.com/kamranahmedse/developer-roadmap







-------
github paper site
-----------
https://github.com/papers-we-love/papers-we-love





-------
mysql client aotomatical finish
---------
https://github.com/dbcli/mycli
--------
github start rank
---------
http://github-rank.com/star
----------
How to find out “The most popular repositories” on Github? [closed]
---------
https://stackoverflow.com/questions/19855552/how-to-find-out-the-most-popular-repositories-on-github
-------
bootstarp
--------
https://github.com/twbs/bootstrap

--------
python to exe schema
----------
http://www.pyinstaller.org/








------
wei   hui




--------
xz unzip
--------
How do I uncompress a tarball that uses .xz?





-----------
人的一生真的非常奇妙，上一次还是在新疆腹地，




-------
awesome list
-----------
https://github.com/sindresorhus/awesome
--------
online anthing to mp3
---------
http://audio.online-convert.com/convert-to-mp3
-------
python github get file
---------
https://stackoverflow.com/questions/14120502/how-to-download-and-write-a-file-from-github-using-requests
----------
------
python u  solu
----------
--------
Why running a python file doesn't require the execute permission?
--------
https://stackoverflow.com/questions/35865758/why-running-a-python-file-doesnt-require-the-execute-permission
------
python How can I reverse a list in python?
---------
https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python







---------
someone
----------
i will use method to 

-----------
python
--------
python send email


#this is from https://www.youtube.com/watch?v=gzv183G9Vew
#this is used to send email
import smtplib
content = 'this is from mryang via mailserver'
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('yang756260386@gmail.com','f!d@i#s$')
mail.sendmail('yang756260386@gmail.com','785582851@qq.com',content)
mail.close()



---------
python
---------
when sublime occur problem,i can slove the format problem via upload file to
github and git pull from linux vim
ofcourse ,you can slove the problem via windows vi
------
python Accessing the index in Python 'for' loops
-------
https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
--------
i canot find the inspiration fro startup.


----------
someone
----------
今天第三次刷<life in a day>,记得第一次刷的时候我还在新疆，苍凉的戈壁，壮丽的风景。那个时候想的是一定要好好珍惜每一天，爱那些珍贵的人，能在离开新疆的时候没有什么遗憾，整个四年也过得非常开心，但也因为各种各样的原因留下了各种各样的遗憾，毕业走的那天乌鲁木齐的天空一如既往非常的蓝，当飞机起飞后，干燥的山头上竟然还有皑皑白雪，心中烦恼和遗憾似乎消失





----------
people
---------
for myself,i dislike to lsiten others to say somethings 
--------
someone
--------
i should give youtube-dowload warn 
---------
someone
-------
i have find i can use web to express my idea.in fact,i feel that 
i need a ios app to advance the ability for mobile and 

---------
someone cs
------------
i need to add info from  mobile,i have the fellowing
ideas ,such as ,send ideas to server and server parser 
the info add the info html

-----------
someone
-----------
i believe that life is so beautiful and i need to experience it  


---------
someone
--------------
the current undetanding is that everyday-----project---------in(drwaer)

--------
someone
--------
i have feel that i have losted to control of the book,that is,get thing done

--------
someone
--------
i find that when i look forward a things ,i always imagine too much !!!!ccc
---------
someone python
---------
use python to craw the a complex page to genreate all kinds of pages
may be ,i can use send info method or say to post data to somewhere
to generate data




-------------
how to download the thepiratebay videos
------------

https://www.youtube.com/watch?v=pLx84Kq0mpE



-----------
someone
---------
every time i make a greate step ,it will the past system.
--------
torrent
----------
https://github.com/jackpal/Taipei-Torrent


------------
someone
-----------
i find that when u donot understand the basement of a problem.
ur query is may wrong!!!!

------
video download
---------
https://telecharger-videos-youtube.com/en

youtube-dl -f best https://www.youtube.com/watch?v=w_lCi8U49mY

------
python
---------
it seems that u cannot import all from a directory pacakage
that is,from a import all 233even if it ok,you wwould can not
use it

---------
startup technique
-------
https://github.com/rg3/youtube-dl/issues/8490



--------




---------
freewriting
-----------
torrent search engineer

-----------
someone
----------
may be i can download the 
--------
someone
--------
i feel that it will be so diffcult to accept other's critism

--------
about torrent download
----------
https://github.com/rg3/youtube-dl/issues/8490


------------
baiduyun automatical upload
------------
use the function,that is ,baiduwangpan automatically to backup   a directory


--------------
python  directory pythonpath
-----------
You need to add your new directory to the environment variable PYTHONPATH, separated by a colon from previous contents thereof. In any form of Unix, you can do that in a startup script appropriate to whatever shell you're using (.profile or whatever, depending on your favorite shell) with a command which, again, depends on the shell in question; in Windows, you can do it through the system GUI for the purpose.

superuser.com may be a better place to ask further, i.e. for more details if you need specifics about how to enrich an environment variable in your chosen platform and shell, since it's not really a programming question per se.


--------
video eddit
----------
http://www.openshot.org/
--------
python __init__.py
---------
https://stackoverflow.com/questions/448271/what-is-init-py-for

--------
Why running a python file doesn't require the execute permission?
--------
https://stackoverflow.com/questions/35865758/why-running-a-python-file-doesnt-require-the-execute-permission



--------
linux
----------
>> is used to appended ,> is used to refresh and add
for example ,ps smip.py |grep smip.py >>test
---------
open source
-------
help the disable http://www.e-bility.com/links/software.php
--------
self learn
--------
https://en.wikipedia.org/wiki/List_of_autodidacts
--------
  for k in range(100234432):
      os.system('git pull origin master')
      time.sleep(10)
      all=getfileeverylinetolist('yangming')
      print(all)

--------
python
---------
as international guide,



----------
python oo
----------

In [35]: class A():
    ...:     a=3
    ...:     b=4
    ...:     def __init__(self,f,g):
    ...:         print 'hello world'
    ...:         a=5
    ...:         print a
    ...:         print self.a
    ...:         print'i am  in __init__ method i will sum f+g,the sum is %s',str(f+g)
    ...:     def test(self,a,b):
    ...:         c=self.b
    ...:         print c
    ...:         print(a+b)

a,b is class level variable,use and modify them,you should use self to point the function
and the a ,b in __init__ function and test function is function  argument,use them
u only need to use a ,b .derived from a  class ,u can rewrite a method use same function
name!!!!

class a:
    def __init__(self,a,b):
        self.a=a
        print(self.a)

-------------
english how to ask in english
---------------








--------
book
----------
1.the pragmatical thingking and leaning
2.a mind for number
3.Elon musk
4.How to get what you want
5.The little go book
6.dechuan jiakang
7.the power of habit
8.the hard thing of hard thing
-------
python bussiness
---------
remove watermark maybe is a business


------





---------
cs  linux command
----------
scp example
scp -r /root/testdir root@192.168.0.181:/root/
scp test.pyt root@192.168.0.181:/root/

-------
hn book
--------
It gets suggested all the time, but How to Win Friends and Influence People is my answer. No other single book will help you out more in life.


-------
 cs git version back
-------
https://stackoverflow.com/questions/4114095/how-to-revert-git-repository-to-a-previous-commit
------
cs
-------
fpm is a strange website.!!!
--------

-----
redis
------
redis must refresh all values









--------
someone
--------
poor is the things that i mostly dislikely
-------
cs 2016
---------
1.many tab
2.build myself tookit
-----
someone
----------
maybe,i should note that we should observer
the china and look for chance and use tech to chnage the
situation.i believe that ..........
------------
--------
someone
---------
1.make use of the things you have learned
2.develop good habit
3.learn how to learn
4.learn how to think
5.luck lady help one who try.
6.do not repeat yourself.
7.think more and make use of discipline.
8.eat the frog first but self-descipline ,that is ,you should not expect
  that you can quickly finish all things.accroding to my experience.long term
  persist will beat  the temporary inspiration
9.every time,you always have some harvest.although it is just a little

-------
someone
--------
i can get inspiration from the  industry conference and look for chance.
the work of dealing with video all occur in my brain
--------
-------
someone
----------
in fact ,i always doubt that caton
can not give my expected salary ,that is,about,8000
,i even doubt .........
--------
someone
---------
many thngs prove that people alaways believe the things they prfer to believe
---------
someone
----------
i find that so many things i want to learn so that i cannot to palce
my energy in correct  place.

------
someone
--------
i find that so many things i can do can bring profit.but i  have no
a silent mood to deal with it!!!

-------
someone
---------
i must admit that sometimes,some problem can be sloved by math,such as the countdown time
------
someone
---------
i must honstly admmit that
when i slove aproblem.is it necesary?
through many things.i find that
when u slove aproblem via all kindds of experiment
and hard working ,but the things donnot give or
stay to keep your passion too long !


-------
someone
--------
i remmeber the time ,when iam middle school,i want to wear a fake face to give
the the feeling of Secret to my colleges

--------
someone
---------
a small company where has a bad man will result the team effctivity!
the lesson come from  the fact ,that is,wangfang is a bad woman
-------
someone
---------
my perfect view,that is ,for example,when i deal with
atom pluggin i have mastered a solution (embed the subtile
  to the video ),but i alaways want to look for a good way
  to load subtitle

---------
-------
someone
--------
i find that when u start a work ,the
pain will disapear mostly
-------
someone
---------
such as ,use ml to detect the users is using vpn
service for goverment.it is a business that
so few people can run it
-------
someone
---------
when i open so many threads .i will distracted
by so many thinds ,for example.when i wanna to read
many book ,i will explode!!!!




-------
someone
--------
when u to slove the problem people want to slove ,you will get profit

-------
someone
--------
communicate with my mother ,i always enlarge fact

---------
someone
--------
i find that my probelem in tomato technique is that
when i finish a 25 minutes slot,when i enjoy the
rewards,i canot stop!!!!!
-------
someone
--------
be carefully,you may waste your time
-------
someone
---------
when i am doing somethings ,my attention is always distracted to
the not very important thingd in the current sdituation
--------
--------
someone habit(have developed)
----------
1.try different route
2.diffuse mode
3.many tab technique
4.plan
----------
---------
someone
---------
my thought is so complicated!!!!!!

------
------
somone
--------
in fact,i need to rethik the siutation my nation located ,not all
things is bad for me,from some point
--------
someoene
---------
how to get profit?
-------------------






-----------
hacker news book
-----------
1.get things done
2.the art of learning
thwe two book is always mentionds by others.
-------
2016-2017
---------
0.fudan
1.chengdu
2.english
-------
ask problem
----------
1.alternative to samba?



---------
170626
---------
1.25 try to start my work
2.15 try to finsihsen coder part
--------
170627
---------
1.25 try to satrt my work
2.35 write my help script
3,25 write  help script and words 10 minutes
4.25 mail problem and download
5.25 encoder problem


------------
hacker news
-----------
the site give me so many things.

--------
someone routine make use of the things you have learned
---------
1.plan in the yesterday and last week
2.use anology and metaphor!
3.freewriting
4.all get somethings every time
5.tomato tech
6.eat frog first
7.recalling the things before see somethings
[--this is so big--]8.make use of the things i have learned
9.make use of the diffuse mode!
10.try to set the finish time.

--------
--------
someone
----------
is there a reason  that i always want to finish any detail of a things
such as,i always need full screen!!!!


-------
someone
--------
i need to design a method to get tourism vertificate !!!!
--------
iphone full screen
--------
please query the key word in itunes app store full screen

----------
someone
-----------
i must communicate with others








---------
python delet afile and dir
--------
How to delete a file or folder?

https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder


--------
cs
--------
i should learn to make use of all kinds tools.







--------
youtube alllinks solution
-----------
u can use all kinds of chrome extension to extract link and
use reg to extract u want
2.use python crawer




-------
book category
-----------
Startups and Business
Philosophy and Psychology
Autobiographies and Biographies
History
Evolution, Science and Medicine
Logic and Problem Solving
Politics
Economics
Sexuality
Education
Writing
Theater and Film
Fiction
Health
Design
---------
There are some books I keep coming back to when I am "feeling lost and/or hopeless", when my "back is up against the wall and/or feel cornered", when I feel like I have "hit rock bottom" or I just need to "escape reality"... This list contains books I have read/listened to more than a couple times:
!For inspiration:! 1. Loosing my virginity (Richard Branson) - Richard Branson's Autobiography. From student magazine to Virgin to crazy ballooning adventures and space! I keep coming back to this when I feel like I need a morale boost. There isn't an audible version for this book, but there is a summary-type version on Audible "Screw it, Let's do it"- does a good job curating the exciting parts.
  2. The Everything Store (Brad Stone)
-AMAZON and the man leading the massive team behind it. Jeff Bezos is quite easily one of the most important and influential people in the world. His relentless pursuit to build Amazon (& it's various products) amid constant setbacks, losses and naysayers... I personally use Amazon and their products every day. It's a really interesting view of how things are run backstage.
  3. Steve Jobs (Walter Isaacson)
- One of the most popular books in the Valley. Almost all startup founders I have met has read this. They usually have a very polarized view of Jobs after reading this. Take the good stuff and leave out the bad/crazy. Jobs was a very polarizing person and so is his biography...This is a very long book. "The second Coming of Steve Jobs" by Alan Deutschman is another really good book and a much shorter read and not super-polarizing (leaves out some of the crazy stuff from early life). Other notable Steve Jobs books I have read & highly recommend: Becoming Steve Jobs & The Steve Jobs Way.
  4. Elon Musk (Ashlee Vance)
-Another polarizing book. I am a Spacex & Tesla Fan-boy. I picked this up in 2015 the day it was launched! I have read this at least half a dozen times by now. Hard-work, perseverance and creativity to the max. A must read for every entrepreneur.
  5. iWoz (Steve Wozniak)
-If you are a technical-founder, this is a must read! Gives a very interesting view of- behind the scenes at Apple during its inception and early years. I was really moved by how humble Woz was/is and I am inspired by his problem solving approach.
  6. How Google Works (Eric Schmidt, Alan Eagle & Jonathan Rosenberg)
- A very good book to read after/before this: "In the Plex" by Steven Levy. Hands down the two most important / influential books while you are starting something new. I read these while I was contemplating conceiving my startup and giving up the "safety" (illusion of safety) of a "normal-job". A must read for anyone planing to start a company and want to take it to the stratosphere (or higher)!
  7. Dreams from My Father (Barack Obama)
- Another polarizing personality. A short but powerful memoir by Obama. This gives a unique insight into Obama's thought processes. Most people can relate to this and every "Leader" must read this. It really helps clear some of the fog on- what makes an effective leader.
!Business & Management:!
  1. The Upstarts (Brad Stone)
-An amazing story about AirBnB and Uber. Culture is key and culture is defined by the Founders and the first few hires. The two companies are extremely similar in many ways (timing, shared economy, disruptive) but radically different in the way they are run. This came out earlier this year and is probably one of the best "startup-books" of 2017!
  2. Zero to One (Peter Thiel)
-A very short book, a must read for every entrepreneur. Dives into "first principal" thinking & execution. A very good read after/before "Elon Musk" the biography by Ashlee Vance.
  3. The power of Habit (Charles Duhigg)
-I have always wondered how successful people get so much done. They have the same amount of time as everyone else, but they are able to get so much more done...how? This book answered that question. Ever since, I have been using "Habits" as my ultimate personal tool. Day & night difference when you figure out how habits are formed how they are broken and how you can influence the process. A good companion book (from the same author) "Smarter Faster Better".
  4. How to win friends & Influence people (Dale Carnegi)
- I bought this book freshman year in college. I tried reading it then and gave up / got bored after the first few pages. I really wish I had actually made an effort to read the whole thing. It sat on my shelf collecting dust. Luckily I picked up the book again and gave it another shot. I read this during a particularly "rough-patch" at our startup- really helped me cope with the "situation". What was once a boring book is now scribbled with notes, bookmarks and highlights. A very useful life-guide.
  5. How to win at the Sport of Business (Mark Cuban)
- A very entertaining yet eye-opening book. It is very short, finished it in a couple hours. A must read for every entrepreneur. I keep coming back to this when I feel like things are going dreadfully slow and I need a boost. If you follow Mark Cuban's blog, skip this. It is mostly a summary of his blog posts.
  6. Finding the next Steve Jobs (Nolan Bushnell)
- Finding good talent and retaining it is probably the single most important thing you will do as startup founders (especially if you are the CEO). Many things in this book seem obvious (if you are familiar with the Silicon-valley culture). A good read before you set out to hire your dream team of "rockstars". A good companion book: "Outliers" By Malcom Gladwell.
  7. The hard thing about hard things (Ben Horowitz)
-Are you in a startup? If the answer is YES, then read this NOW. Ties well with "Finding the next Steve Jobs". I wish I had read this before I started my company. I have lost track of how many times I have listened to this audio-book.
  8. Start with the Why (Simon Sinek)
- Mid-late 2013 I came across Simon Sinek's ted talks on the golden-circle and my mind was blown. I bought the book the very next day and I keep coming back to my notes whenever we are starting a new project. Get the "Why?" right and the product will define itself. This is true for building companies as it is for building great products. A must read for every entrepreneur.
  9. Art of the Start (Guy Kawasaki)
-Getting ready to pitch? read this! Also watch Guy's many presentations/talks on YouTube. A good companion book- "Pitch Anything" By Oren Klaff
!Escaping Reality! 1. Hatching Twitter (Nick Bilton) -Sooooo much drama! Definitely learnt what not to do! Very interesting read.
  2. The accidental Billionaires (Ben Mezrcih)
-I have heard that not everything in this book is "completely-true" (more distorted than others...) but still a great read!
  3. The Martian (Andy Weir)
- Hands down the best science fiction book I have read. I have lost count how many times I have listened to the audio-book (probably >15). I want to go to MARS!
  4. Harry Potter Series.
-My go-to "background noise". I read the books as a kid. I use the audio-books to tune out the world when working on stuff that does not require my full attention (Listening Goblet of Fire as I type this)...
  5. Jurassic Park || The Lost world (Michael Crichton)
- Read the books as a kid. I usually listen to it while I am traveling. Still gets me as excited as it did when I first read the book. (The movies are nothing compared to the book...)
  6. Ender's Game (Orson Scott Card)
- I am looking forward to reading the entire series. Read it once, listened to it many times (lost count). I love Space!
  7. Ready Player One (Ernest Cline)
-I picked this book up while I was working on a VR project back in 2014. An excellent book for re-reads and a nice place to get some inspiration.
!Other honorable mentions:! Actionable Gamification (Yu-Kai Chou) I invented the Modern Age (Richard Snow) Inside the tornado (Geoffrey Moore) Jony Ive (Leander Kahney) Sprint (Jake Knapp) The lean startup (Eric Ries) The selfish Gene (Richard Dawkins) Titan (Ron Chernow) The inevitable (Kevin Kelly) The Innovators (Walter Isaacson) Scrum (Jeff Sutherland)
!Most if not all have an audio-book version!
If you are in a startup or plan to start one soon, reading/listening to books should become a routine. I try to get through at least one book a week, sometimes two.
Good luck!
---------
hn book
--------

vecter 2 days ago [-]

How To Be A 3% Man by Corey Wayne [0]
I'm 30 now. I wish I had read this when I was 20. It would've made dating in my 20s so much easier. I came across it last year and it's probably the single most important book I'll ever read in my entire life, for the sole reason that understanding women will allow me to have a successful marriage one day. I cannot recommend this enough.
[0] Free online: https://www.scribd.com/doc/33421576/How-To-Be-A-3-Man
reply
------
source how to change mysql password
--------
#!/bin/bash
echo "=============================Enter installazition================="

#install dev tool
yum -y groupinstall 'Development Tools'
yum -y install python-devel
yum -y install jemalloc-devel
yum -y install epel-release
yum -y install wget
yum -y install psmisc



#install database
yum -y install mariadb-server mariadb
yum install MySQL-python -y



#install  redis-server
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
(cd redis-stable&&make)
(cd redis-stable&&./src/redis-server --daemonize yes)


#config mariadb password
systemctl enable mariadb
systemctl start mariadb
sleep 5
mysqladmin -u root password "123456" >/dev/null 2>&1
systemctl stop firewalld






#install python-pip
sudo yum -y install python-pip

#install redis client moudle
sudo pip install redis
sudo pip install requests
sudo pip install flask



echo "=============end all course========================>"

------
arxiv
-------
this is a paper site
------
170602
--------
1.25 start my work plan.and words
2.25 finish link status update.
3.25 finish all kinds of link.
4.25 finish yesterday task of reading a mind for numbers
5.25 prepare start the work.adjust the stream
6.25 intergrate the ivp
7.25 try to start ivp wrok.
8.25 ivplink
-------
170605
--------
1.prepare to start my work and start download youtube video.
2.25 finish youtube download
3.25 read a mind for  number 10 pages.  
4.25 side project and money.
5.25  try to remember  words 10 minnutes.
6.25 profile grammar and alarm start .
7.25 start to test another device.
-------
170606
--------
1.25  prepare to start to work and 10 minuts words
2.25  try to write main borads status.
3.25 english phrase and jude if the device it  is working.
4.25 deveto 25 min to a mind for numbers.
5.25 devote 10 minutes and start to look for verb phrase.
6.25 phrasal verb solution.
7.25 try to modify malfunction device link status
8.25 redisgn all kinds of device except
9.25 tidy smip.py
10.25 test smip.py function
11.25 check smip 195 status.
---------
170607
---------
1.25 words 10 min and verb phrase start.
2.25 redisgn the smip.py
3.25 try to configure samba configure tool.
4.25 try to  change smip.py
5.25 try to change smip.py
6.25 try to chnage smip.py
7.25 change smip.py
8.35 change smip.py
9.35 change smip.py
10.25 slove a device except situation
---------
170608
--------
1.25 prepare to start my work and words recitement
2.25 test smip.py
3.25  test smip.
4.25 check single device status if it  is ok
5.35 finish single device link
6.25 try to tidy the logic of  link.
7.25 prepare complete link.
8.25 optimiseze the link
9.25 get the smip rx.
10.25 debug th recevive rx
11.25 debug rx
------
--------
170609
----------
1.25  try to start work
2.25 tidy the link
3.25 test the link.
4.25 test the link,
5.25 try to adjust the link.
6.25 try to package
7.25 test package to install
8.25 try to slove password problem in installation process
9.25

---------
170612
1。25 start my work ，deal with the all kinds of part1 3 subtitles。
2。25 TEST project testproject。
3.25 test install package
4.25 test install package
5.25 test install package
6.25 test install package and download 5 title
--------
170613
---------
1.25 try to use youtube to grasp the vargrant tech.
2.25 virtual box and vargarnat configure
2.25 virtual vox tech
3.25 ivp monitor installation
http://shunyi_repo:8000/yangming/ivp-monitor.git
4.25  test the installation package
5.25 test install package
6.25 install test package
7.25 clear all key
8.25 subtitle
--------
170614
----------
1.25 listenningskill for subtile
2.25 prepare to start work
3.25  try to start debug slow problem
4.25 try to debug encoder.py
5.25 try to finish the slow problem
6.25 try to slove smip problem
7.25 try to slove python except line
8.25 try to debug smip info
9.25 test the install group
10.25 words 10 minutes and 10 subtitles.
11.25  down load fudan title
---------
170615
-------
1.25  chinasubtile
2.25 chinasubtitle
3.25 try to slove the ivp all problem
4.25 words 10 minutes and youtube 30
5.25 fudan subtile and korea
---------
170616
--------
1.25 try to start my work
2.25 try to update my private repo and start to debug
3.25 try to get command outpu  in python  adn start write a stop
4.25 try to start debug
5.25 try to slove the bug
6.25  try to start all info
7.25 try to the last ivpinfo
--------
170619
---------
1.25 try to design a week plan and the day plan
2.15 try ro start ivp all task
3.15 try to design the task of warn.
4.25 try to rethink the alrm design.
5.25 update the device status
6.25 update  device status
7.25 debug link status
8.25 update single device status
---------
170620
----------
1.25 try to read a mind for umbers 10 pages.and 10 minutes words
2.25 try to start python course.
3.25  try to stop server
4.25 try to stop the service
5.25  try to work with college wang
6.25  try to end all task in today
----------
170622
---------
1.25 youtube-dl video
2.25 try to start to design the routline
--------
170623
-------
1.25 start my wrok
2.25 10m words





--------
170629
--------
1.25 start my work
2.15 try to study reglar expression
3.25 try to write youtube subtile script
4.25 deal tith subtile script
5.25 try to deal with subtitle video
6.25 try to start slove subtile

--------
cs comamnd line in a page
---------
the command line in a page ,it does work



------
0719
-------
1.try to invertigate python asynoums







-------
ivp warn
--------
A.detect device
1.network if work!
2.
B.detect link
1.the expeted link does not work
2.
----------
how to extract images from a web
-----------
https://www.youtube.com/watch?v=ct15QXBGIJE
inspect----source----imagines

------
someone
-------
i must see some new things to refresh my insight!!!





----------
someone
---------
i always expect more beutiful thing,but i canot do the current thing well.
---------
someone habit routine
--------------
the fellowing is the habit i have developed or wanna
[ok]1.read book for great chance
[ok]2.make a plan daily and longer
[ok]3.try different routine
[ok]4.use toamto tech to battle with protication
[--]5.try to make use of the things i have learned
[ok]6.freewritting
[--]7.form and use my routine to slove problem
[--]8.try to desgin the today the plan list in yesterday
[--]9.in the learning course,try to use anonogy
---------
cs future
----------
i must think that
-------
youtube
---------
https://youtu.be/YsBN8miDWXU
---------
python os system commands get output
----------
Running shell command from Python and capturing the output
https://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output
--------
someone
---------
did i give up looking for soul-mate
di igive up look for soul-mate?
-----
SOMEONE
--------
i can think of the time,that i cannot read the vb shaolei source code
although the process only have 300 or more line code,this also happen in
the work or other situation,but in the now,i doubt that  i have no
a good plan to slove these things.

---------
-------
somone
----------
the world includes so beautiful things ,bu i have no so much time to digest
them,i feel so pityful!i feel that my inner heart is so thrilled or i donot
make use of the things i have leaned!









-------
python
---------
i can get insight from pycon ,i will becomer top pythoner








-------
someone
---------
now .i need to rethink how  can i applied the knoeledge
--------
someone
---------
the power of habit is always be mentioned in all kinds of corner.

-------
someone high shcool
---------
in high school,i ever do timer management.but it does not work ,i guess that  
the env does not allow to do private things.
------
someone
--------
you must think when you should be a exploer,when you should be a fellower?
---------
someone
---------
when i am in trouble,i must undertsand that what is my problem?
---------
someone hacker news
-------------
the hacker news website include so much effctive info
so that i think that i have not time to ingest so much insights!!
is it happiness and sad?
---------
cs hn==hacker news
--------
The Pragmatic Programmer by Andrew Hunt and David Thomas
this book is always mentioned by all kinds of pepole.
- Code Complete by Steve McConnell
- The Effective Engineer by Edmond Lau
- The Pragmatic Programmer by Andrew Hunt and David Thomas
reply

--------
cs chrome pdf
----------
you can make use of chrome print funtion to produce a pdf.
-------
someonen     
--------
from some views,in fact ,i try any so many method,why i have get these outcome?????
i think that i want to be quick but negelted so many things.
such as ,middle school time,i write so many exercise ,but it does not
work,i feel that i just want get the illusion of complete.




-------
english
---------
Phrasal Verb is a obvious problem.
https://www.youtube.com/watch?v=oUWTubehtE0 this may be
a good link for the topic

---------
hn book
---------

novalis78 1 day ago [-]

"How to get what you want", by Raymond Hull. Everything else follows, like a bootstrapping process. Wish I had found it 10 years earlier. Changed my life forever. I could recommend dozens other books, my walls are lined with shelves of books, but you and me are different and all you'd need is this one book to find everything else you'd need to read or do.
--------
Hackers and Painters from Paul Graham. I wish I had read that when I was 14 years old.
reply
-------------
someone cs
-------------
if i can quickly build a new env ,
i can do all kinds of exp.
----------
words solution future
------------
i can build a map to form a sloutiin to remember words

---------
python email
------------
1.receive form data
2.use python to send info to private mailbox




-------
someone
-------
i have no desire of anything right now


---------
python get youtube-playlist all url
-----------








--------
cs important
----------
1.grasp the techque of quickly generating a new env
2.grasp the fron technique
3.grasp the Phonetic



-------
zero to one
---------
in fact ,the book ,that is, zero to one ,i feel that when  i finish the reding of it
.i have undertand my english have space to develop









------
170719
-------
1.25 try to start my work and 10 min words
2.25 heroku affairs and test
3.25 try to test asyn request and inverstige request asyn
4.25 test asyn
5.25 try to test grequest
6.25 TRY TO EDIT GREQUEST moudle

---------
english  of
----------
two cups of water
a piece of paper
the door of home



-------
network
--------
the bandwidth i donot undestand always puzzled me !!!!



------
discuss
-----------
2.setup env(git,heroku,vpn,)
1.gtd system()
3.try to read the first paper(about blockchain)
4.discuss kexinyun(about blockchain)







------
BITCOIN blockchain
--------
https://www.igvita.com/2014/05/05/minimum-viable-block-chain/

--=---
someone habit
-----------
1.try different routine
2.make a plan
3.diffuse mode
4.always get somethings
5.recall somethings
6.tomato technique
7.reading book


---------
blockchain
------------
https://news.ycombinator.com/item?id=12571287








----------
from my current situat
------
Ask HN: What is your favorite YouTube channel for developers?
---------
https://news.ycombinator.com/item?id=12702651







---------
red full-stack language
----------
http://www.red-lang.org/p/getting-started.html



--------
hacker news books
-------------
The Subtle Art of Not Giving a F*ck
Think Like a Freak
SmartCuts
reply
Deep Work.
How to Win Friends and Influence People.
The lean startup. How to win friends and influence people.
--------
someone
----------
according to my exp,the diffuse mode does work!!!!!!!!
-------
ahcker news
----------
The hard thing about hard things. Horowitz the book is always mentioned in all kinds of situation
----------










-------
redis cs
--------
How do I delete everything in Redis?
https://stackoverflow.com/questions/6851909/how-do-i-delete-everything-in-redis


------
python
---------
print except info is great .espically you have designed except
mechenism


--------
python except print except info
------------
https://stackoverflow.com/questions/3702675/how-to-print-the-full-traceback-without-halting-the-program

import traceback
import sys

try:
    do_stuff()
except Exception:
    print(traceback.format_exc())
    # or
    print(sys.exc_info()[0])



------------------
somputer vison
-------------------
https://www.youtube.com/watch?v=40riCqvRoMs&t=7s
-----------------------
python translate
----------------
https://pypi.python.org/pypi/py-translate

--------
startup
-------
there is some source for exploring new directions
argxiv,github,












-------
python
---------
i need to understand that how does python setup.py work?





------
video someone
--------











-------
python cs
---------
i need to intergrate all info to a scripts.
-----------
someone
-------
每一个夏天
从2012年夏天开始，每一个夏天总有美好的事情发生，昨天我重走5年前
走过的路，世纪钟下面的小猫爱小花，爱到复旦关门已经被擦去了，也不知道
小猫还爱着小花吗抑或还在一起吗，结婚了吗，组成幸福家庭了吗？池塘里面
取走的水现在还留在新疆，那个神奇美丽的地方，浩瀚的风景，燥热的夏天
小伙伴一直催我回到新疆取回那瓶水，那瓶水当初还被任勇喝了一口，也不知道
池塘里面的泉水味道怎么样，也不知道他还和当初的小姐姐怎么样。我在新疆
度过了人生中非常美好的四年，
6月的上海
老是下雨，5年前来的时候也在下雨，如今又在下雨，又一次在这个校园里面
迷路，树荫还是那么茂盛，想起四月份来一个很厉害的老师的实验室面试...
当年给读者杂志投的稿件似乎没人理会，也不知是那时的无病呻吟还是歇斯底里
让该杂志看不上，还是在那时整个社会开始被科技带的飞速发展，人性开始浮躁
看不上我那样的愣头青，没有黄段子，不会讲故事，不会熬鸡汤的文章吧。
早上翻到了大学好友的状态，竟然已穿越过塔克拉干沙漠，见过干枯的胡杨林
，也不知道这些胡杨林有没有像书中所说沉睡千年，却依然风华正茂。
新疆是浩瀚风景的故乡，我还在天山脚下游荡，便匆匆离开。后来常想，一个诗人
要是去过新疆得用处多么雄浑的诗篇，长河落日就可见一斑，即便有一日再
归去重游故地，还是少时风景吗?花有重开日，人无再少年的惆怅个日日夜夜浇筑
着关于新疆的美好和遗憾。

-------
why i hsve the disire to do the things completely?
-------
business how to ask
-----------
1.what do u want ?
2.can u give the data to prove that ur right?


---------
python Permanently add a directory to PYTHONPATH
---------
https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath

---------
python
-----------
when except error ocuur ,i should print the except info.or
it will bring many trouble


-------
python except info
------------
https://stackoverflow.com/questions/1483429/how-to-print-an-error-in-python


---------
shell
-------
Temporarily change current working directory in bash to run a command [duplicate]

https://stackoverflow.com/questions/10382141/temporarily-change-current-working-directory-in-bash-to-run-a-command

-------
vargrant
1.use right contorl in keyboard to exit vitual box caspture

-------
python and ping
---------
https://stackoverflow.com/questions/2953462/pinging-servers-in-python
---------
someone
---------
i think that formiing  a habit is very important.that is ,because it will decrease willpower waste.
--------
someone
-------
??????what i want to say?my english vocbulary is .......
-------
someone
---------
i must care about that why i cannot get things done?such as python core
code ,i have the plan but i have not fineshed it!!!!!
-------
---------
someone speaking
----------
speaking is a kinds of art !!!!
------------
someone
----------
in fact , i feel that i donot need to ask others
some problem.because ithink that i can slove the  problem
vi reading book
------
-----------
someone
----------
i must admmit that the book do benetfit me greately!!!!
i must learn how to manage the time to absorb all kinds

of slight
-------
--------
someone
-----------
i must quickly form my set tech stack!
--------
someone book
------------
,i need a book about psychnology to know
my all kinds of problem and mood state activity
--------
someone
--------
may it be ,chnage the routine of daily it work ,i feel that it give the inspiration of to
slove the problem of ivp

---------
video  tech stack
----------
https://news.ycombinator.com/item?id=14475884
-----------
book hn
------
https://news.ycombinator.com/item?id=14477851
--------
hacker news
---------
How To Win Friends And Influence People by Dale Carnegie - a timeless classic for people skills, useful in almost all circumstances.

-------
python Get the string within brackets in Python
Extract string from between quotations
--------
https://stackoverflow.com/questions/8569201/get-the-string-within-brackets-in-python
https://stackoverflow.com/questions/2076343/extract-string-from-between-quotations


------
someone
-------
what if the vpn  is forbiiden?????






--------
book
--------
get things done this book is always recomended!
-------------------
someone slove problem
------------------
1.look for old archive tidied by myself
2.look for youtube etc video tutorial
3.look for literal tutorial
4.ask sb who master the tech.
5.use money to this things.
---------
someone
-------------
i find that i always want to do cool things but it doenot bring some
profit!!!!
--------
the construct project
-----------
https://www.planradar.com/
---------
business
---------
http://stephaniehurlburt.com/blog/2017/6/24/on-starting-a-software-business
--------
hn book
-------
https://news.ycombinator.com/item?id=14477851
https://news.ycombinator.com/item?id=14486657

-------
someone
---------
i find that i dislike to write stuff in paper when i start to use pc.

-------
cd programmer guide.hacker news
-------------
https://news.ycombinator.com/item?id=14486657
--------
english
---------
i need to learn frequent english phrase.
----------
python
---------
def check_ping(ivpid='test',ip='test'):
    if ivpid!='test':
        ip=parserip(ivpid)

    hostname = ip
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

you can add any argument to lead the capality of function     
-------
think why we think our thought is obvious.
------
https://sivers.org/obvious
-------
someone
------
may it be ,i should read the amzon review of a mind of number.
-------
someone reading
----------
why reading.
https://goel.io/why-read/
--------------------
side project future
--------------------
https://news.ycombinator.com/item?id=14039135


-------
python  words schema
--------
How do I read a file line-by-line into a list?
https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
-------
python string padding
---------
How to pad a string to a fixed length with spaces in Python?
https://stackoverflow.com/questions/20309255/how-to-pad-a-string-to-a-fixed-length-with-spaces-in-python

-------
python excel column schema
---------
Create nice column output in python
https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python
https://www.reddit.com/r/learnpython/comments/1vd3j8/how_do_i_output_my_print_statements_to_a_text_file/
-------
someone
---------
when i slove aproblem.yeah.i can  give many solutions.this is about diffuse mode.but
when i slove a problem using a method.i find that i can not deeply to explore
this method.in fact ,i find that this method is effective,
-----
someone
---------
i find that ,most time ,i donot obey the  law or say discipline ,
what is going on?
--------
170602
---------
1.25 start my work set
2.25 try to slove productivity problem.
3.25 words deal with .
4.25 python write words to a file
5.25 slove words solution
6.25 words solution
7.25  the link status.
-----------
python rename file
------------
https://stackoverflow.com/questions/2759067/rename-files-in-python

-------
python install develop package
--------
https://stackoverflow.com/questions/6230444/how-to-install-python-developer-package



-------
comic web
----------
https://xkcd.com/1066/
-------
someone
---------
in fact,my coutry and developed world has so many difference.i think of that i can fullly make use of the gap
-------
english
--------
https://news.ycombinator.com/item?id=14447885
i may be become any expert in language.
------
english
----------

https://buildmyvocab.in/
-------
youtube
-------
only download audio for english from youtube.
-------



------
python mysqldb
--------
https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip


--------
How to install Python MySQLdb module using pip?
--------------------
https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip
--------
redis run in background
----------
https://stackoverflow.com/questions/24221449/want-to-run-redis-server-in-background-nonstop

-------
someone
--------
in fact ,i feel that all kinds of chances always exsists.from taobao view,if i can get customer
requests.i will get 1 profit.
-------
someone
--------
i believe that the freewriting tech will mostly help me ,because i think that
only reading many  books is not enough.when i deal with the all kinds of
info .i mostlt get spicial effect in my brain.i may understand knoeledge .
i may get insight.

--------
someone
----------
one things that may be vey perfect.but when i listen its bad things,i will feel very frustrated.

9.25 simulation many ivp device in server
----------------------
youtube

------
possible json given by wangyifan
-------
{"errorcode": 0, "ivp_list": [{ "id": "ivp201704120540","ip":"331" ,"solt_list":[{"solt0":[{"name":"dddd","status":"noboard"}]},{"solt1":[{"name":"ddddd","status":"bad"}]},{"solt2":[]},{"solt3":[]},{"solt4":[]},{"solt5":[]}]},{ "id": "ivp20540","ip":"ddd" ,"solt_list":[{"solt0":[{"name":"dddd","status":"noboard"}]},{"solt1":[{"name":"ddddd","status":"bad"}]},{"solt2":[]},{"solt3":[]},{"solt4":[]},{"solt5":[]}]}]}





----------
blockchain
-----------
https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d
-----------
crypto blockchain
-----------
https://cranklin.wordpress.com/2017/07/11/lets-create-our-own-cryptocurrency/



-------
python
------
i meet a strange bug the print function can not work ,but the code donnot
give error clue.
-----------
somone how to learn
---------
i may understand what th book (a mind for numbers) said.when you have the
basic knowledge ,you can use diffuse mode to make full use of it
------
someone
-------
you can use a puzzel(pingtu ) to exercise kids' imagination


------
someone
-------
i always  doubt that the present seem like that happened  in the past.
----
business
------
i can open a business to deal with all kinds words .the theory is to use
regular expression .
------
subtitle  how to delete a line that begin with a digit in linux
sed one-liner to delete any line that begins with a digit
------
170523
------
1.document fudan affairs and lawyer safairs
2.mr wang yifan and db
3.35 chinese vlc.and make plan.
4.25 preapre to start my wrok./plan and words
5.25 try to set encoder table.
6.25  try to set decoder table
7.25  try  to set smip table.
7.25 create smip table.
8.25 try to write all kinds of exp data.
9.25  try to understand nosql
------
170524---------
1.25 prepare to start my work.and recite words.
2.25  try to understand redis quick start
3.25 try to write info to redis in python and start a new script
4.25 try ro get a smip boards info.
5.25 slove tomato solution
6.25 tomato solution
7.25 try to tidy the script of connect ivp
8.25 break down the ivp scripts
9.25  try to break down all ivp scripts

------
170525
--------
1.25 try to start my work.tidy my disk in work pc
2.25 try to debug ivp smip info
3.25debug the ivo smip info
4.35 debug ivp info
5.25  try to get link
6.25 try to get the link
7.25 try to give the ivpid of smip rx
8.25 try to give the device of ip
9.25 debug link info
10.25 get decoder smip source


=======
170527
-------
1.25 stackoverflow ipython solution
2.25 stackoverflow ipython solution
3.25 stack overflow ipython solution
4.35 slove a mind for number test solution
5.25 25 min reddit
6.25 give the linfo
7.25 10min words and db detach
8.25 try to detach encoder decoder code.
9.25 give the linklist
-------
170531
---------
1.25  try to get lookup alldevice id
2.25 try to tidy single device link test
3.25  try to give single link in ivp.
4.25 try to tidy all ivp single link
5.25  try to adjust single ivp info package
6.25 tidy decoder info.
7.25 give all info in single ivp
8.25 give all info of pos
9.25 give every device pos and status
10.25 device status and pos.
11.25 finish positions and change link info


----------
170524
------
5.25 try to get encoder source and smip ge the half link
6.25 try to test encoder source
7.25 try to get the smip link



-------
python
----------
https://www.liquidweb.com/kb/enable-epel-repository/
https://www.liquidweb.com/kb/how-to-install-pip-on-centos-7/
------
python
-----
you can use the functionname(a='yangming'),set arguments priously

------
somone
-------
my cough include sputum,this is  not idea.i must note the
problem.
---------
someone
--------
i must learn my learn type. and i must make use of somethings  i have learn.

-------
1.document test  
-----
cs
------
symbolic link is a very sad problem.
------
vlc language
------
http://www.ihaveapc.com/2011/08/how-to-change-the-menu-interface-language-in-vlc-player/

------
vlc
-----
chinese subtitle solution .https://www.youtube.com/watch?v=WTdVbiJYwZE
https://forum.videolan.org/viewtopic.php?t=80
401
------
cs  json  format
-----
cs python
--------
from my experience. i should give example result in every palce that may include result
-----
srt file
--------
https://www.youtube.com/watch?v=7410wF49qKs
-----
170522
--------
1.25  paln.start add the column in
      infoofivp table.ready for start to work
2.25 integrate ivp working status.   
3.25 debug the working status function.
4.25 GIVE THE error code interface and try to write encoder info to db (encode/decoder.)  
5.25 try to update the corresponding groupin ivp
6.25 give the all pos and status.      
-------
someone
-------
where can i get the reuirements of users?
-----
someone
------
i believe that the tech industry includes so many chance.
-------
someone
--------
i must face the reality of my character.

-----
someone
-------
i thin that i need to audit every paln ,that is,how to start ,when to start,when to finish
,via my ability i can set a conutdown timer for my plan
-----
someone
-------
i must increse the ability of deal with all kinds of pratical problem.or
i will lost confidence of deal with all kinds of problem
-------
english and somone
--------
i find that when i meet a problem,that may fuck my comfort zone ,i may lost
patience.such as the ugly doc.
-------
my view is that the ability is not that the colorful but not
pratical tech.i must grasp the tech to service my learning.
----
cs someone
------
i need a tech to show my someone private documents
besides.i must quickly master a tech oto stand by
our carrer.
-----
database
------
give single db
give the cursor
use get row
seresbea 
yRBE4t3TcK

seresbeauty123
username: amandaxl88

pin:093620686
https://github.com/kootenpv/yagmail


---------
python 
--------
i can use the python read a file content to another content
or use git to pull a file to another git repository









--------
email setup
---------
https://github.com/kootenpv/yagmail

seresbeauty@seresbeauty.
------
chenniao
--------
http://git.chenniao.com/users/sign_in
--------
vpn
-------
the current speed is singopera is the the best!
-----
stackover flow cs
--------
i can answer the question

-------
bitcoin  blockchain
----------
any node can be seen as arguments.
no center is a revolution
blockchain have the flavor of share economy


------
someone
--------
i must admit that the fact,that is, my eye ability is decresing
































--------
video writing
---------
i can desgin  a player that i can watch video while i am reading






------
cs python
------
you can use os.system to excute system command!!!!
such as marco ,can be doable
-------
ipython
--------
i master ipython configure tech
such as ,
find ipython dir
use these urls
http://stackoverflow.com/questions/15403523/where-do-i-put-ipython-configuration-files
http://ipython.readthedocs.io/en/stable/development/config.html
http://ipython.readthedocs.io/en/stable/config/intro.html?highlight=config%20
!vi ipython_config.py
# sample ipython_config.py
c = get_config()

c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.log_level = 20
c.InteractiveShellApp.extensions = [
    'myextension'
]
c.InteractiveShellApp.exec_lines = [
    'import numpy',
    'import scipy'
]
c.InteractiveShellApp.exec_files = [
    'mycode.py',
    'fancy.ipy'
]
c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'LightBG'
c.InteractiveShell.confirm_exit = False
c.InteractiveShell.editor = 'nano'
c.InteractiveShell.xmode = 'Context'

c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [
 ('la', 'ls -al')
]

exit ipython and restart ipython
-------
i must addmit that the english listenning skill is become the bigggest obstacle for me to
quickly slove problem.
----------
inverst plan
------------
1.evaluate how much money we need
2.conifirm we will get money from who?
3.write all ivps positions info
-------
170515
--------
1.25 start plan today test color.week plan
2.25 python color solution
3.25 windows cmd and ipython ansd start ivp
4. ipython tips
5.25 start noon work
6.25 try to slove vi problem and alias
7.25 try to slove alias problem
8.25 read ipython config file
9.25 ipython config file
10.25 ivp all decoder of boards ends
11.25 ivp all info debug
12.25 ivp regitered info
------------------------------
youtube resolution solution
------------------------------
https://askubuntu.com/questions/486297/how-to-select-video-quality-from-youtube-dl
---------
someone
-------
the  focus mode may alaso be toxic,for it allways
repeat your old method.this may not work when meet
a new problem,this problem is seen from my high shcool
time,the bad grades and the dongchen time,the physic teacher
also say these  things.such as empty cup method.my teacher
tell me that you sholud empty the knoeledge that you have learn.or
he would teach more things.
------
someone
---------
make fulll use of the things i have learned.
-------
python install scrapy
------------
https://stackoverflow.com/questions/22073516/failed-to-install-python-cryptography-package-with-pip-and-setup-py

-----------
startup .furture
-------
when you are a indie developer,you may need a laywer as assistant
------
170517
-------
1.25debug mysql connect
2.25 upload my yangdb to github./write every devcice data./set time gap function
-------
database
--------
MySQLdb this moudle is onley for linux !!!!
--------
170518
------
1.debug
2,25 debug
3.25  test all kinds of speed
.
------
may i write change what we said.
--------
170516
--------
1.25 start my work
2.25  try to recited words.and rethink the days
3.25  test encoder and decoder.
4.25 test decoder and encoder
5.25 study database of frequncy words
6.25 test decoder and encoder.
7.25 try to design end solution.
8.25 test encoder and decoder.

------
how to study
----------
Question everything.
Reading recent hidstory
Of science Of computers Of the cold war Of the second world war Of communism
Reading about what knowledge is and how do we reliably create it?
What is knowledge?
What are facts?
What is data?
Reading about areas outside your area, sociology
Social psychology
Also knowing only tools and no content will make you a technician at best. Knowing stuff about how the world works, what knowledge is and how we got here will make you a valuable colleague, leader, parent, friend.
Source: started liking school towards the end of high school, ended up another 6 years in universities.
Focus on finding out why you struggle with it and address those weaknesses
-------
cs html
-------
we do learn html all kinds of stuff.
------
how to study
---------
The Art of Learning
------
I've read a mind for numbers by Barbara Oakley, fantastic book which helped me immensely while studying engineering mathematics. Highly recommended
------
english
------
i must admmited that
my english need to learn hard ,ther are so many fact to falicite me to think so
such as ,reading hacker news  is al little hard for me.listengning stanford course
is also hard.i am feeling depressing.whne i am  reainf /listenning e course .
i feel that these coutdr i hsbr domsnu words i donnot undersyaf ;be side,therese orequestio is beru annoued
i feel that the words  of these course most i donnot understand
<<<<<<< HEAD

------
python cs
-------
about a languge ,my ideal is that
the function ,loop ,judgement(maybe , assert).single instruction.is the basic
elementary of the tool.
-------
someone
-------
i must tidy all kinds of resource i have learn
-----
someone
--------
building the community is a good idea.that may be the root of budiness.
------
cs someone html
=======
someone
--------
mr zurkerbug said on one knows what to do in the begin,only when you start a
things ,you know what should do
https://www.youtube.com/watch?v=4VwElW7SbLA
------
cs mysql
-------
according to mr wang xue wen,mysql should use many table to store array but.
-----
in fact i donot understand the ajax tech and js ,why did we say
that ajax does not load the page.but js reload the page.when js
use the tech ,such as,getelementbyid.it refresh the tab.the other
things does not change.of course.there is a function you need note
,that is,setinterval.i know it is for updedate some stuff.but the
page it will be get from the server.???
------
learn how to learn
-------
the brain has 2 modes.it contain focus mode and diffuse mode
about prostocation ,the teacher has a advice ,but i remmeneber
that when i am bechaor time.the pro psychology,when you start a
thing just 5 minuts ,you will adpted it .you mostly to do the things.
but  e experience i have not adapted.
about procrastinator.the tomato way is a way all mentioned bu all kinds of occassion.
in fact .the pro is main real reson.
out pro,the first 20 minutes is painful.but when ,if you can persir the  stage you  should
feel thet the pain will .the pro adivice that we use 25 minutes as a period to work.when you finish
the period ,yu can relax !!!
exercise is a good point or wat for your study
practise help convert temporary memeory to long-term memory
besides,about the peolple of lacking attention is may creative in many fields.

imposter syndrome is very common feeling.that is,you think that what u get is not worthy belonging to u
there are 2 views taht is ,test and homework is best methods that help you learning more!
but the method obey my method ,that is ,make things happen!
recall is a very important tool to build knowlege map ,just for example,when you reading a material,
you reorganize the material via recalling ,besides,about the tenique of simplify /anology is alwasys
mentioned such as feyman,if you can explain the knowledge to your grandfather well,you will be ok in understand
the material.there is a method mentioned,that is ,insert yourself to the problem !!!!but this is diffcult to understand   


about passion.passion is about things you are good at,but u should not follow your passion,many things need time
to be skiiled or say you are good at it,so you should broden it .well!
the teacher may recommen d abook,that is , a mind for numbers.!!!!
reading the complex material ,you may slown about it ,but it is  a reality,if u are quickliy,you will lose somethings.

---------
english
------
i have a idea,that is,in fact ,i think that i need to remmember many words.
for some reasons.i feel painful ,but i doubt that ,for some reason.i think
that learning driven by pratical probllem is more effective.of course,i can
write a script to remember words.
---------
cs db
-------
in fact,database also manipulate file.
-------
someone
-------
i find that i may misundertand or donot think the purpose of who said the things.
--------
html cs
--------
i feel that the structure is fellowing:


built-in method strip of str object at 0x7fe7d7a963a0> is not JSON serializable
http://stackoverflow.com/questions/16720882/python-class-method-return-name
-------
online json parser
---------
http://json.parser.online.fr/




--------
someone learn
---------
the metaphor and anonogy always mentiond in the a mind for number and
the pragrmatical thingking and learning
--------
cs css
------
how to change css color
http://stackoverflow.com/questions/21919478/how-to-change-the-background-color-using-javascript
-------
someone
-------
i bielive that if you can use computer as a tool ,
your live will be recorded and analysis more scientific
-------
css layout
---------
https://css-tricks.com/quick-css-trick-how-to-center-an-object-exactly-in-the-center/
------
learn
---------
I think for a lot of people who struggle with learning the problem is two parts, first you have no idea how to approach something, or no consistent strategy for how you actually pick up things and second the discipline is not there, mostly because your brain as it is is not wired to learn effectively.
--------
psychonogy
---------
when you start a thing,you will contribute more time.
--------
future
--------
i need to understand where the market is ???

------
world video website
http://radio.garden/live/hamilton/y108/

---------
cs database
-------
when you use db as data center ,all logical in client ,you must
note that who write data to the database,so there ,it is impossible
,in server endpoint.you only use a single db.such as you need a  script
to write  content to the db.
-------
cs
-------
it seem that client showing pages all take html and js and css technology
---------
cs
------
i must understand how the front work with together!

-----
csch
--------
subtitle solution gain subtile
python
--------
 for filename in os.listdir("."):
     try:
         if filename.startswith("[gainsubtitles.com]"):
             os.rename(filename, filename[20:])
     except:
         pass





-------
subtitle solution
-------
http://gainsubtitles.com/search/g
-------
we can use a  database in center and place all logic in client.this may be a good solution
------
youtube subtitle solution
--------
https://www.quora.com/Is-there-a-way-to-extract-the-automatically-generated-subtitles-in-YouTube
------------
What is naming convention for subtitle files?
https://superuser.com/questions/346599/what-is-naming-convention-for-subtitle-files






-------
ipython show source code
----------
https://stackoverflow.com/questions/3143888/is-there-a-way-to-view-the-source-code-of-a-function-class-or-module-from-th






------
reading
-------
elon mask book always related to the man https://en.wikipedia.org/wiki/Howard_Hughes and stve jobs.

------
cs
------
i find that i  donot understand function programming very deeply.
-----
python
--------
can python write the execute sentence  before the funtion
------
ipython
-------
i feel that i need to learn ipython some interseting tips.
------
youtube red
-------
you can purchase youtube red accounts
------
yotube
-------
subtitle shcema http://diycaptions.com/php/get-automatic-captions-as-srt.php?id=0VhLVaIKKgA

--------
json example
--------
[{'id','2017','boeardslist':[{'slot0':{'type':'decoder','name'}},{'slot1':{}},{'slot2':[]},{'slot3':{}}]

--------
python baiduwangpan upload schema
-----------
https://github.com/houtianze/bypy

-------
python html schema
--------
https://github.com/grangier/python-goose

--------
web wechat schema
------------
https://github.com/liuwons/wxBot
--------
python voice speech schema
----------
https://github.com/Uberi/speech_recognition

--------
comunicity
-----------
https://github.com/discourse/discourse
redis python
-----------
someone
----------
i need to ckeck my sex desire,what is wrong ?



-----
someone
-------
if you slove a problem ,it has many sloutions.
you need to rethink which way is
-------
words solution
---------
1.read a word from source(file/database)
2.ask if you can remember the word
3.count the times of every word if you (not) understand the word
4.save Statistics data to somewhere.(file/database)
5.according to statical data to feed words to user().
-------
words solution
--------
extract everyline to  database .design the tables as fellowing

word   explanation thetimesofunderstand  notunderstandtimes thetimeofuse   loadtime

-------
fortune
------
pdf2word
youtubedl
txt extract and words analysis
--------
sole softwaree
--------
we can let user to try out my extension.if it is well ,i  will ask use pay fee.
------
python
--------
for k in range(5):
    shanghai='all'
shanghai variable 's function range
--------
t531w618095 497003
------

-----
ted
-------
donnot say your private goal.
------
python flask
--------
you can use *args to set many arguments even 0
when you visit api ,you donot need arguments but when you directly
use the function to use.
------
algorithm
-------
how to think algorithm ,this is a very impotant line.input-------black hole-----output
in fact,the black hole is a good algorithm.
---
cs
-------
i decide to change my method.via to add 1 to the words i can rember
and use regx to filter
-------
someone
-------
about stupid risk.st least,from now opinion,i find that
i may lost my brain to do somethings seen as stupid
for example.i want to go sichuan to fetch my t-shirt
but why can not i think that the fee of the trip.the fee can buy somany
t-shits.
-------
someone
-------
how to make use of time efficiently,it seems so urge!!
if you can grasp how to learn quickly and efficeintly
,i guess i will quickly get success.
------
someone
------
if the things we go to school is to learn how to learn.i may miss more
------
someone
------
form my experience,if you are error in big direction,you will be lost in all kinds of  troubles.s
-------
someone
------
i find that i 'm scared to anticipate competiton.such as i worry
that  when i low the price of taobao service,i will attract more
programmer to compete with me .this situation is more in all kinds
of situation.
------
someone
-------
about humanble,i understand that the root is poor.
------
cs  words delete a file
-------
0.detect a file how many lines in a file
1.read a line use loop
2.use a varibriation to receive the content
3.command to ask if you remmember the words
4.use command to delete the line if you reply 'yes'(you should use count schema)
5.switch to the next line.
-------
someone
-------
from some view.i like teaching myslef.i dislike teachers ,why??????
--------
someone
-------
when you slove a problem,you should think that
what is the upper problem domain.such as the problem is includeed by a big problem

-----
someone
-------
according to someone of ted.you always wait a moment that you want to do anything.the comfort
zone is very mad zone
-------
someone
-------
why i dislike homework??????only for  i lack discipline????

----
someone
-------
when i want to do a thing,my inner seem to be fired.or  it may be anxiety!

------
someone
-------
in fact ,i have a desire to write a software to recite /remmenber words,but i have a worry that
i can not persit ,besiedes,long implement process
will disburb me!
-------
someone words
----------
1.fetch words and detect you rember the words?
when you say the words is too smiple  up to 3
times ,i will delete it in the file and add it
to the note (have recited ),besides,when you
say that you have understand the words up to
20 words ,i also implement the above action ,that is,add the word to have-understand notes.
the sofware also can give counting the words .the
index include you have master etc.we also can detect are you really undertsand the words ,in order to implement the goal ,we extract the words
from have-undertsand notes to ask you if rember?
when you donnot understand the words ,we invoke
the online api to get the  explanation,
-------
someone
-------
what is critical thinking mentionsed in all kinds of artices?








-----
stanford behavior
----------
1 espido
--------
the goal of the course to avoid thinking category to study human behavior
use 3 famous people to sai that the bucket thinking,the most famous is newyork subway
the teacher laughs the people seeking peace that was related to india.
the teacher also say a famous experiment that when we give some any env you want ,you can
elevate


----------
2 espido
-----
cs  stanford course  deal experience
---------------------------------------
1.use youtube-dl download videos and subtitles
2.use linux command   cat * > merged-file to merge all file      to merge all files
3.use linux command  grep -o -E '\w+' temp | sort -u -f|tee all.txt to extract all words
  to a file (such ad all.txt) ,you can use the txt file to load all words to recite.
  or.for all kinds of goals
special:is there a subtitle producer/buider to  modify subtitle

4.you can use a technology to merge all words to finish some goals ,such as stanford's teacher lecture notes.
5.you may use python to rename all kinds of files in a directory

'''
for filename in os.listdir('.'):      
    a=re.findall('\d+',filename[0:4])
    os.rename(filename,str(a[0])+'.txt')

'''

6.according to order, i will merge all file ,in the case,i merge the final stanfordbehavior .txt file.

for k in range(25):
    os.system('cat '+str(k+1)+'*'+'>stanfordbehavior.txt')


for k in range(25):                                                                                 
   file=file+str(k+1)+'.txt '


to get cat file list comand! to merge to aa file [success]


english
------
\i

------
english
=-------
when he author use a metaphor in english ,i feel so suck,because at any time,i lost direction.s

----
fortune
------
i find there are 3 ways i can get money 1.exchange goods to make money from difference
2.write a app distribute to market 3.youtube video download 4.pdf to word
5.finance 6.teaching

someone
--------
you must addmit that


-----
cs
------
what is short/long link??


----
ted :how to stop screw your life.
------
0.it is very simple but not easy
1.in fact ,you never feel that you will like to do any thing
3.out of brain ,past feeling
4.5sbase




-----
business
--------
Over time, I learned that being an intern publicly and a mentor privately was essential, since no one wants to be criticized in a meeting by someone who sounds like their dad.
------
someone
------
ask why and what if ,these views is always mentioned in all kinds of occasions




study
-------
i design a route to get a great position

------
stanford
-------
stanford has many inrideable pro ,such as https://www.youtube.com/watch?v=NNnIGh9g6fA&list=PLMwddpZ_3nkAWijQlBnkwnr9wfcuderVe ,besides,




------
cs
-----
indiehackers seem to be a website that in china doesnot exists.
---




------
fd
------
fudan,urumuqi,shanghai,xinjiang,nanshan,dongchen,




--------
cs
-------
when u test server ,you can use client such as restful client  to test server .




future
-------
robot,i believe that in the future ,the robot will have version and i
may get good chance in the future.after all,robot get brain,you can
get great profit.
------



------
future
-------
make a list review website to reviw every part of tv.





cs
------
in the usage of post,you should post your data in the body of request .
-----





cs
------
why we need to use restful api????


----
economy
-------
when someone's productivy up,he is worthy more crwdit.these cridit len to barrowers who can use it to consume
,you need to understand ,one's spending is the income of someone else.so this link is wvery important.


-----
future.
-------
so,i can not afford the basic requirement.so,i feel so hard to stand the
cridit card.i must to look for a new way to get money.

-------
network
--------
i doubt get method that donot have body .but when get-method get response ,the response has body .



-----
economy
-------
debt /cridit is main part of economy.but central bank  control the money in the society
.whenrecession and inlation,central bank control the rate to stimulate  people
to barrow  money .in the case,when rate is low,people
prefer to lend money .besides,someone's
spending is another  one 's income .this is very imprtant info .

---
someone
-----
may it be ,i may not  to face future and forget past .so that i can not cherish today.
such as goulidan.such as jiasu.such as the test of high shcool.
------
someone
-------
from some view,may be my communicate skill is not awesome.i need to warn
-------------
someone
-------
when my opinon was opposed by someone.i will feel depressed

-------
someone
--------
i may admit i  must make use of all ability to compete .not using single skill.


------
someone
-------
i need to think that discipline and prosticator is same things?
---------
----
cs
-----
i download so many great videos,but i doubt if i will wahtch them!




future
-------
in fact.i can add brain to tom that can say.this is a good boy.

------
english
--------
the preposition of english is a drawback of my english.
------
english
--------
the main drawback of my english is that i used to think in chinese .
------
future
------
i hope that when i graduate from fudan ,i can startup a company.


-----




someone
-------
in fact,i feel that mr yao is good ,may it be,my state is not so open.
-----
future
-------
i hope after graduting from fudan.i can forster a startup company.
from tech and bussiness ,it is success.
-------
bussiness
-------
i can sell havard cs class.




--------
youtube
----------
i  can use youtube-dl in us server to download video and slice the video and download in cn .
-------
fund
-------
i want to turn mymoney(including credit card) to my wealtth accounts to inverst
----

------
package simple tool
---------
https://github.com/jordansissel/fpm

------
fdexam
--------
array
------
use vector as array
struct Edge{
int nextnode;
int cost;
}
vector <Edge> edge[N];


0.c++ mode
using namespace std;

1.from now situation.i need to graps basic tree manipulate and graph manipulate.


from my sit:uation.fudan 's proramming test i need to grasp
1.how to get input
int a,scanf("%d",&a)---------how to get int
char b[50],scanf("%s",b),but you need to note that-------->how to get char
printf("%c",b[30]),printf("%s",b)

2.how to use  queue and stack and vector.
in these implemented algorithm ,you can use
a.you need to load the package(^---^ )
  #include <vector>
  #include <queue>
  #include <stack>
b.in finishing above steps,you can use them as int or char;
  stack <int> a/queue <int > b/vector <int>      
c.using the data struct .
  a.push(3)  queue.psuh(3)    heap.push(x)   how to add  data to vector  
  a.pop()    queue.pop()      heap.pop()
  a.top()    queue.front()    heap.top()
  a.empty()  queue.empty()    heap.empty()

3.how to use array ,it is a potional danger
struct node{
  int a;
  int b;
  void testfunction(int a, int b){
  printf("you have inputed %d\n",a+b)
  }
}yangming[63] .

it will create array it has 63 elements with struct


4. in fact ,you must note pointer when you use.
   pointer style is
    int *a
    char *a
    node *a
  when use in function ,you need to note that
  i will use a example,
  node * test(int a,int b){
   node A;
   A.a=3;
   A.b=4;
   A.testfunction(3,4)
   return &A
  }

  you need to know how to pass pointer to function
  int a,b;
  function(int &a,int &b)
       {
        *a=7;
        *b=8 ;
       }

  it may be string.

5.from the position ,i have no other worrys.
6.sort function , you need to using it.sort(a,b+c,compare)
7.you need to note pointer position.such as a[17].
a+5,it denotes sort ,sort 's parameter is cmp that return a bool.

8.about string ,you need to note that what is a clue of the ened of string?
  from now view,it is char[i]==0.you also note that
  the action about string such sa
 char a[35];
scanf("%s",a);
a='yang'
  strlen(a)==4?
  char b[35];
  strcopy(b,a)
  strcmp(a,b)

i also need to note that how to use include <string>


this situation is need to note
struct node{
  int a;
  int b;
  node * c
  node D?????///this is illegal?????


};

strcpy(s1,s2) s2 to s1
strcat(s1,s2) concatenates; s1+s2====python
strlen()
strcmp(s1,s2);s1==s2---0,s1>s2 ------->0,otherwise
strchr(s1,ch),find the ch char pointer ,it is ,a position;
strstr(s1,s2),return a pointer to the first occurence of string s2 in s1;


i may worry about link list implements.


string operate code
char b[30];
scanf("%s",b);
printf("you have input %s\n",b);
printf("you need to care about your input 's %d\n",strlen(b));
printf("i will test string end indication\n");
int i;
for(i=0;b[i]!=0;i++){
printf("length is ==%d\n",i);
continue;
}
printf("string length is %d\n,i bet b[i]==0,in fact is %c",i,b[i]);
char c[100];
strcpy(c,b);
printf("now c's value is %s\n",c);

11.priority_queue<int,vector<int>,greater<int> >q;
   this is big heap implement
12.i need to master binary tree costruct  method.
  how to make a binary.
  first ,middle,rear iterate methd.from main view,i find that.data structure
  is
  struct node{
   int a;
   node *lchild;
  node *rchild;
  };   
 void preiterate()

iterate method is following:

struct Node{
Node *lchild;
Node *rchild;
char c;

} Tree[50];
int loc;//have allocate memory number;
//----------initiate node---------------
Node * create(){
Tree[loc].lichild==Tree[loc],rchild==Null;

return &Tree[loc++];
}



//------postorder--------------


void postorder(Node * T){
if (T->lchild!=Null){
postorder(T->lchild);

};
if (T->rchild!=Null){
postorder(T->rchild);


}
printf("%c",T->c);

}

other iterate methods.you need to steemulate ,but you need to
chnage print order;


-------
operate binary tree
#include <stdio.h>
#include <algorithm>
using namespace std;
struct Node{
Node *lchild;
Node *rchild;
int  c;

} Tree[50];
int loc;//have allocate memory number;
//----------initiate node---------------
Node * create(){
Tree[loc].lchild=Tree[loc].rchild=NULL;
Node * nodeposition;
nodeposition= &Tree[loc];
loc=loc+1;
return nodeposition;
}

char str1[30],str2[30];

//------postorder--------------
void postorder(Node * T){
if (T->lchild!=NULL){
postorder(T->lchild);

};
if (T->rchild!=NULL){
postorder(T->rchild);


}
printf("%d",T->c);

}

void midorder(Node* T){
if(T->lchild!=NULL) midorder(T->lchild);
printf("%d",T->c);
if(T->rchild!=NULL) midorder(T->rchild);
}



/**
Node *build(int s1,int e1,int s2,int e2){
int ret=Node *create();//for the tree's root allocate memory
ret->c=str1[s1];
int rootldx;
for (int i=s2;i<=e2;I++)
{
if (str2[i]==str1[s1]){
rootldx=i;
break;

}}

**/


Node* insert(Node *T,int x){
if (T==NULL){
T=create();
T->c=x;
return T;
}
else if (x<T->c)
 T->lchild=insert(T->lchild,x);
else if (x>T->c)
  T->rchild=insert(T->rchild,x);
return T;

}

int main(){

int n;
while (scanf("%d",&n)!=EOF){
loc=0;
Node *T=NULL;
for(int i=0;i<n;i++){
int x;
scanf("%d",&x);
T=insert(T,x);



}
printf("post order is \n");
postorder(T);
printf("mid order is \n");
midorder(T);

}



return 0;

}






```



















```
复旦大学软件学院2017年全日制硕士研究生复试名单公示


考生编号  姓名  初试成绩  外国语成绩   政治理论成绩  业务课1成绩  业务课2成绩  复试专业
  102467210009974   代超  348   69  64  91  124   083500 软件工程
  102467210009971   刘霜  334   57  61  93  123   083500 软件工程
  102467210009731   徐锐  334   69  63  110   92  083500 软件工程
  102467210009872   黄霖  333   77  61  101   94  083500 软件工程
  102467210009648   裴朝翰   324   65  64  100   95  083500 软件工程
  102467210009970   杨明  313   75  53  86  99  083500 软件工程
  102467210011246   孙振远   393   84  64  119   126   085212 (专业学位)软件工程
  102467210011279   夏腾  392   73  69  130   120   085212 (专业学位)软件工程
  102467210011237   王欣  377   70  58  137   112   085212 (专业学位)软件工程
  102467210011249   孙若宇   375   72  65  113   125   085212 (专业学位)软件工程
  102467210010368   王政和   363   80  64  136   83  085212 (专业学位)软件工程
  102467210011249   李长辉   352   70  58  119   105   085212 (专业学位)软件工程
  102467210010690   桂钰坤   346   79  60  102   105   085212 (专业学位)软件工程
  102467210010695   任俞锦   340   76  55  95  114   085212 (专业学位)软件工程
  102467210011257   周鹏程   339   68  62  100   109   085212 (专业学位)软件工程
  102467210011364   雒齐  334   77  58  81  118   085212 (专业学位)软件工程
  102467210011267   邹宜霖   330   73  52  127   78  085212 (专业学位)软件工程
102467210010556   邱庆帅   330   82  65  101   82  085212 (专业学位)软件工程
  102467210010317   刘洋  329   69  53  113   94  085212 (专业学位)软件工程
102467210010345   刘昕伟   328   71  63  98  96  085212 (专业学位)软件工程
102467210010519   郑贞杰   328   66  56  109   97  085212 (专业学位)软件工程
  102467210010480   刘凡  327   74  59  104   90  085212 (专业学位)软件工程
  102467210010306   孙伟  327   73  62  95  97  085212 (专业学位)软件工程
  102467210010384   陈世泽   327   75  60  104   88  085212 (专业学位)软件工程
  102467210010646   许鑫星   326   71  51  112   92  085212 (专业学位)软件工程
  102467210010601   胡远文   325   67  53  112   93  085212 (专业学位)软件工程
  102467210010453   戴婧  324   75  59  103   87  085212 (专业学位)软件工程
  102467210010658   梁文杰   323   73  65  90  95  085212 (专业学位)软件工程
102467210010663   陈镜宇   323   69  55  116   83  085212 (专业学位)软件工程
  102467210010319   张志坤   322   74  54  99  95  085212 (专业学位)软件工程
  102467210010569   高健  322   77  62  83  100   085212 (专业学位)软件工程
102467210010363   施亮  321   67  55  90  109   085212 (专业学位)软件工程
  102467210010413   陈家豪   320   82  63  93  82  085212 (专业学位)软件工程
102467210010573   李孝川   319   69  56  113   81  085212 (专业学位)软件工程
102467210009786   谢怡亭   318   74  51  103   90  085212 (专业学位)软件工程
  102467210010301   乔颖  317   70  58  98  91  085212 (专业学位)软件工程
  102467210010478   温智灵   312   76  60  95  81  085212 (专业学位)软件工程

















-----
network
-------
i have no strong desire to study my internetwork,mr wang's problem-driven
is the key of desire.
=======
------
uc-berkely
---------
i fell uc berkely 's influence.for them remove youtube 's course have influence
so many people in hacker news.
------
health
--------
i should vare about my throat situation,for it  last 3 years.
-----
someone
----------
i wnat to write a konwledge map engine.
------
someone
--------
i find that i lost my way sometimes in the internet ,i donot feel
my eenrgy and interest.

------
someone
------
i need to live in international hotel to bring  new story to my life
------
interview
--------
in interview,i feel that my konwlege is not enough.so .i donot get
great job.
----
hbr living
-------
https://hbr.org/2017/03/if-you-want-to-be-happy-at-work-have-a-life-outside-of-it
------
python
-------
i think my python consists :before outputing result,what deos python interpreter do??string and byte,unicode,python all method.what in-memory
actions is??

-----
python
--------
python interpreter is composed of compiler and vm.compiler produce
bytecode ,vm excute bytecode to produce result.

----
resume
-------
strong english read ability.
database buckup project
database lookup tool

-----
python
--------
heroku run the step pip install -r requirements.txt
------
interpreter
---------
in  interpreter  ,there is all kinds of interpretes,usual implement is
lisp interpreter.i believe python implement python interpreter is
very usual.
-----
resume
---------
i can implement a python interpreter using go lang
i understand the classical python interpreter how run source code
i understand run a python program in mmemory all actions.
i understand python program call graph.
i grasp all python algorithm
i write a lisp interpreter use python

python
-------
there are intepreter and compiler ,the interpreter will proccess source code
and run the result of processing,donot need to transform source code
to machine code ,the aboving machine code is compiler work by compiler.
-------
python
-------
i think i need to know python interpreter how to work ,becuase , i donot be get
used to gap the stage of how python file to be excute?
https://ruslanspivak.com/lsbasi-part1/
http://jayconrod.com/posts/40/a-simple-interpreter-from-scratch-in-python-part-4
http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
http://stackoverflow.com/questions/16808387/writing-my-own-python-parser-and-interpreter
https://csl.name/post/vm/
https://morepypy.blogspot.jp/2011/04/tutorial-writing-interpreter-with-pypy.html




-----
idiom
------
“If you don’t know how compilers work, then you don’t know how computers work. If you’re not 100% sure whether you know how compilers work, then you don’t know how they work.” — Steve Yegge
------
python
-------
.py -----> lexicial analysis  generate token stram------->paser use token stream to make abrstract  tree------>ast will be transformed to bytecode--------vitrual machine run bytecode




------
web
-------
i need to rearrange my we b everyday ,i need to updown the web make new days occur in the topest
web.
------
someone
--------
i must to rethink my communicate  problem ,such as with mr jin ,
------
future
-------
i want to  become apple developer!because i want to connect  apple device to server
!!!!i wnat to  set all kinds  of data in apple device.



------
python
------
i need to rethink ,what is my purpose of i want to grasp well python?/??

-----
english
------
i diske english pro ,such as ,as,down,with,i dislike as.



-----
freewriting
-----
the freeewriting tech do help to understand so many things ,but i hvave no desire to
rearrange it , i feel so tired!!!!i donot get more stroong disre to improve it



------
python
-------
i wnat to jnow python excute a .py script ?what memory occur?????this is my care about problem!!!
in the most recent,i want to know.when i run  a python  program
a=1
b=2
def test(a,b):
    reutrn (a+b)
from csapp view , ithin k memory donot have acllocte for name inly allocate space for value
when meet a function test,which  will vuild a stack ,i understand that is another space
in memory,thet will use csapp theory.FROM  PHD ZHANG,I GET A VIEW ,a=1,a is  not cllocated space and
whe python call a test function ,that is ,then,it will allocate a space.     







ivp
-------
first ,i understand ivp is  a hardware that receiver data ,processing data,output data.form now,receive
data is satelite or brodcat signal to deal with. i understand that  signal as network 's first layer
.paser will unsrstand ------->signal-------->deal signal---------->ouput-------->..fro now,my routeline
is :what is ivp? how to receive salite signal?there is a view,vedio codec is that ,from now
my task ,is to konw that in ivp 's all kins noun is what mean>??????from now , i only need to  call
get method to get infomation,i need to figure out all kinds of items.




-----
python and cs
-------
use mit with python introduce ,or it is a goood ideal
-----
python
-------
may it be ,reference and variable and name is same thing in python
-------
problem sloving
----------
say with a robot or a thing,you can understand /orgnize your puzzle.

------
python
------
i can let my heroku to run my code in  server forever via write code in main.py!!!!
python main.py in hthe hood ,i guess this is the mechinism of heroku
------
someone
-------
it seem that my logic is a little weak!

------
python
------
about python ,i need to build a map of kownledge,my current method is to

-----
cs pdf to word
---------------
http://convertonlinefree.com(best)
https://pdfcandy.com/pdf-to-word.html
https://smallpdf.com/pdf-to-word
http://convertonlinefree.com/PDFToWORDEN.aspx(best)
-------
4300
----
credit card 1309
-----
owe 100 +468 +250=818
----
total 2130
----
bank left=2170
------
fund+god=785
-----
accout 2955
-----
future
------
mr wangwang supply great view about problem-driving ,
----
someone
------
ifeel thet my main problem is that  manage my energy to a things 2.explore all kinds of
direcretion 3.how to applied my owning konledge to a things that will work.

-------
python
-------
https://github.com/Zulko/moviepy
video editing
https://github.com/Zulko/moviepy
---------
business
---------
How to remove watermark/logo from a video? [closed]
https://stackoverflow.com/questions/29196899/how-to-remove-watermark-logo-from-a-video

--------
business
---------
i can understand the user need from freelancer
https://www.freelancer.co.uk/job-search/python-script-watermark-video/
--------
network cs
---------
network is te final stacle for me to climb the spicial realm
----------
python how to split a string to a list
---------
https://stackoverflow.com/questions/743806/how-to-split-a-string-into-a-list
---------
cs
------
i need to make a  frame to orgnize my python konwledge.
-----
someone
-----
python




------
python
------
i konw that python class level variale is called class attribute ,and in __init__
methos we call instance attribute
--------
someone
---------
i find that i disperately dislike to use config file



-----
foture
=======
use video to recird your life ,it is a great ideal,i have find it in university
but i donot apply it,i will use it in next days.

------
SOMEONE
---------
connect the world is the way you feel your exsistence.
-----
someone
-------
i need to check or other my  love view

------
cs finance
---
i can convert pdf and download youtube to bussiness.
-------
someone
--------
you will never feel that you love to do  so


-------
finance
------
finnace is on time and crisis.


------
someone
-------
i have a feeling ,thet is real ,finnace safety ,i have not been owning it
from these years,this point ,i have must to noted.

-----
someone self improving
-----
i have learned a great view,anythings if you need todo,you only
three seconds to thinks ,if yo exceed 3 secnds,you will not
----
slef improving
------
1.keep your blood sugar level
2.sleep in designated time
3.set a break interval during 90-120 /or depend on yourself.
4.
-----
english  read
------
for read view,you dont have to gigure out every word,you only need to guess
,if the word occur again,you need to figure out via tools book
-------
english
______
many executives don’t find ways to practice consistently healthy behaviors, given all the other demands in their lives
GIVEN ====because.




-----
problem slove
-----
in a book about complixity,it use divide and conquer method to
test volume.

-------



                    problem sloving

                 math    economy     cs

                   english    people  


------
book
------
from self contorl view,add blood sugar is very good level.
------
pythonlist
----------
python list concentrate action is composed
by l1+l2 it will produce a new list ,we set a empty list
it is..........[],
for elem in l1:
    a.appended(elem)
for elem in l2:
    a.appended(elem)    
also,i see mit algorithm course ,them say in list operation ,many action
is o(1) complixity.
-----
python
------
detect a class leevl ,you can ask sb how to restrict class instance attribute
,such as a.b or a.b=3 if you need to gurantee this attibute >0????
my now answer is to use descriptor.
------
python
-------
python protocal is a set of method........

-----
python class
------
python class self ,best understand is  that,if a instance was created ,self
is simialr to a instance.in fact ,i feel ,eeven if you created a class,when
define a instance ,you can add a instance attribute,for axample:
class A:
    def __init__(self,bi,lu):
        self.author=bi
        self.title=lu
you can use a=A(67,78),YOU CAN USE a.io='yangmingishandsome'        

----
python
-----
if  i define a class ,i can use a.attribute=5 to reassign a class attribut????
in fact ,it is real ,you can that i have via experiement,read ooficial document
's difficulty is that you may donot have a bluprint of the concept.'
-----
python
-----
imho ,python operator is such as + - /％　ｅｔｃ..
-----
resume
-------
i have bug database of python ,mysql
i can use source control tool

---
someone
---
my opiniopn is that i can use python do anything.
----
openspource
-------
i need opensource to open my career.which director i need?????my
ideal is tohelp others and get  a bunch  of
 margin,now i need to yhink  what can i do use machining learning,what can i do
 via python for marigin?????for nmore great career.

----
nginx
-----
i need to  konw what nginx can do???????
------

someone
------
i think that this summer is the time i left caton
----
image recognization
------
i find the this that it locate the position to find the position's function
when again you stop the postion (coordinate),it will detect the function value is
corresponding the value.
------
python
------
i just want to say that if you  import a moudle that moudle include print('balalabalala')
when you import,the print will  be excute.
-----
python
------
python running a script 's process is that complie a .py ----->.pyc (or other)
bytecode file and python intepreter excute the .pyc file.but i want to know
.py how to be complied and by who??????what i need know is that if python run
a .py file ,for example in a project,python run a hello.py but he invoke other
module,how it work with he hello.py????why open a file and you need close the file???
.of course ,i understand .pyc file is a binary file.
----
world
-----
the worls seem to seek more quick speed.more speed.

python
------
i feel that list in memory is  a array.or it is notassciated
with c's array,i need to understand it vi asking phd zhang.

python
-----
i can feel that python interpreter actions when you run a script or a program ,a=3,allocate memory
??????????????????????????????????????????????a=Classexample(6,7,8).same ,allocate for the instance
,when you can use len(a)(the class implement __len()__ mwthod ),the interpreter see what a is ???
fuck it is a class (i doubt there it activate a mechinism that check  the type object,for instance,
the checked result is string ,it will understnd string class have implemented __len__ method,it will
invoke it,a.__len__() and the return value.) ,it will check if the class include a __len__() method,
if it  include,it will  get the value.if not,it will  give callback error or say it is exception!!!!
.about garabage collection  mechnism ,tha is another thing!!!!!!
-----
someone
-----
when you want to say in writting,you can access your inner.
----
python
--------
i doubt all python object implemented by class
phd sai that python object in python shell(or interpreter ) life circle
is exit python shell.but in function ,wehn function end,the object end ,but
also observe reference count.another info a=[1,23,4,5],when i use a[3]=1,i only in-place (origin list position) change list rather than create a list,but also
spicial situation.you must notice.from my opinion,a=[1,2,3,4,5,6].you can understand that
list is common mutable consequnce,but string and tuple ,string is immutable,what is immutable,
immutable is a[3] if can change origin consequnce value. i can undestand ,when you a=a+b ,id(a) donot equal
origin id(a),but you use a+=[2],id(a) is oriign value.this is same in literaly.you can understand that in-place
as same position but new is not at same position.__iadd__ is the former ,by visrce.
-----
someone
-----
i always believe that there is a method or think tool to help people to slove any question!
-------
book
-----
it may be  a book https://news.ycombinator.com/item?id=12459216
---
network
-----
i feel sad with network??i undestand layer as n protocal in a layer
---
about algorithm
------
https://news.ycombinator.com/item?id=4783301
----------------
how to read a book
------
https://news.ycombinator.com/item?id=12209446
-----
sf  scope
------
I somehow cannot understand the trends, altough I checked following sites and utilized Twitter stats/trends.

* http://www.google.com/trends

* http://www.trendsresearch.com

* http://www.worldtrendsresearch.com/major-trends.php

Here is a general list of ideas that I'd like to pick 2 to 3 from the topics to create a project that is mashing them up in a Ruby On Rails project. It's important to choose only key features of each topic and merge them into one idea.

I don't see the problem that people seem to have according to trends, so I cannot solve it.

Can you please help me with that? I'm searching for a project idea.

Here's a list of Project Ideas I found in the net.

==================================================

1. Business Performance Reporting

2. Case Management for Government Agencies

3. Classroom Management

4. Clinical Trial Initiation and Management

5. Competitive Analysis Web Site

6. Discussion Forum website

7. Disputed Invoice Management

8. Employee Training Scheduling and Materials

9. Equity Research Management

10. Integrated Marketing Campaign Tracking

11. Manufacturing Process Managements

12. Product and Marketing Requirements Planning

13. Request for Proposal Software

14. Sports League Management

15. Absence Request and Vacation Schedule Management

16. Budgeting and Tracking Multiple Projects

17. Bug Database Management

18. Call Center Management Software

19. Change Request Management

20. Compliance Process Support Site

21. Contacts Management Software

22. Document Library and Review

23. Event Planning and Management

24. Expense Reimbursement and Approval

25. Help Desk and Ticket Management

26. Inventory Tracking

27. I T Team Workspace

29. Job Requisition and Interview Management

28. Knowledge Base

29. Lending Library

30. Physical Asset Tracking and Management

31. Project Tracking Workspace

32. Shopping Cart

33. Knowledge Base 34 Lending Library

35. Physical Asset Tracking and Management

36. Project Tracking Workspace

37. Room and Equipment Reservations

38. Sales Lead Pipeline

39. Yellow Pages & Business Directory

40. Time & Billing

41. Class Room Management

42. Expense Report Database

43. Sales Contact Management Database

44. Inventory Management Database

45. Issue Database

46. Event Management Database

47. Service Call Management Database

48. Accounting Ledger Database

49. Asset Tracking Database

50. Cycle Factory Works Management

51. Sales Corporation Management

52. Business Directory

53. Education Directory

54. Dental Clinic Management

55. Fund Raising Management

56. Clinic/ Health Management

57. Cable Management System

58. Survey Creation and Analytics

59. Museum Management System

60. Multi-Level Marketing System

61. Learning Management System

62. Knowledge Management System

63. Missing Person Site

64. Disaster Management Site

65. Job Management Site

66. Financial Portfolio Management

67. Market Research Management

68. Order Management System

69. Point of Sale

70. Advertisement /Banner Management and Analytics

71. Export Management System

72. Invoice Management

73. Recruitment Management System

74. Articles / Blog / Wiki Web site

75. Online Planner

76. Mock Tests and Examination Management

77. Examination System

78. Practice Test Management.

79. Asset Management System

80. Travel Agency System.

81. Placement Management System.

82. Polls Management

83. Customer Management

84. Project Management System.

85. Network Marketing System

86. Yoga Health Care Management

87. Personal Finance Management System

88. Real Estate Management System

89. Stock Mutual Funds Management

90. Careers and Employment Management System

91. Music Albums Management System

92. Classified Ads Managements

93. Property Management System

94. Sales & Retail Management

95. Dating Site

96. Hotel Management System

97. Search Engine

98. Online News Paper Site

99. Image Gallery 100. Staffing and Human Capital Management

101. Address Book

102. Inventory Management System

103. Newspaper Classifieds

104. Hostel Management 105Music , Lyrics Website .

106. Wildlife Safari Trip Management

107. Wildlife Sanctuary Management

108. Wild life Flora and Fauna Statistics Management

109. Animal Hospital Management

110. Zoo Management System

111. Agro-Forestry Management System

112. Bus Depot Management System

113. Even t Management System

114. Clinical Research Management System

115. Food Technology Management System

116. Circus Management System

117. ResortManagement System

118. Bugs/IssuesManagement System

119. Life /MotorInsurance Management System

120. Exam Scheduler

121. Ad CampaignManagement System

123. Internet Banking Management System

124. Ad Agency Management System

125. Vechical Traffic Management System

126. Web Traffic Analytics Management System

127. Solid Waste Management System

128. Peer-To –Peer File Sharing System

129. Chat Application

130. Crisis Management System

131. Disaster Management System

132. Document Management System

133. Security Threats Evolution Software

134. Digital Rights Management System

135. Games ,Single , Multi-Player

136. Content /Document Management System

137. Archaeological Survey Management System

138. Market Research Management System

139. Crime Management System

140. Jail/Prisonmanagement System

141. Telephone Traffic Monitoring Management System

142. School Drop Out Statistics and Analytics System

143. Lost & Found Management System

144. Online Tutorials Management System

145. Bulk Sms Application

146. Criminal Records management System

147. Email Campaign Management System

148. Political Campaign Management System

149. Skill Competence and Mapping Application

150. Ontology based Web Crawler (source: http://goo.gl/Du3ow)
-----
python
------
python switch variable
a,b=b,a
-----
python tuple
-----
tuple 's element is all kinds of types,but immutable
from now,memory is big problem ,when related to redis and python generator
----
login and autication
--------
i undestand that authentication sys is user send username and password,if username and password doesnot
exsit in database,return register html page,user fill info (via form) and click submit(register) ,send info
to server ,and server store info in database,return login page.about  password style in db,imho,should use
hash code style,from my  now,i donot hash and donnot set password policy ,and donnot restrict or say that i donot
know how to protect info 's secure. html.page you can refer to https://github.com/oxfordyang2016/flask-help/blob/master/hello.py
----
html
-----
when you use html form,you can use from element to  implement the function
in from element .there was a things called action,you can use the example to
implement this function .at the same time ,you also note that method can be specify
,imho,post only fro more secure=ly upload data
<form action="http://global.bing.com/?FORM=HPCNEN&setmkt=en-us&setlang=en-us" method="POST">
        <div class="login">
                <div class="login-screen">
                        <div class="app-title">
                                <h1>Login</h1>
                        </div>

                        <div class="login-form">
                                <div class="control-group">
                                <input type="text" class="login-field" value="" placeholder="username" name="username">
                                <label class="login-field-icon fui-user" for="login-name"></label>
                                </div>

                                <div class="control-group">
                                <input type="password" class="login-field" value="" placeholder="password" name="password">
                                <label class="login-field-icon fui-lock" for="login-pass"></label>
                                </div>

                <input type="submit" value="Log in" class="btn btn-primary btn-large btn-block" >
                            <br>
                        </div>
                </div>
        </div>
</form>
of course ,you need to think that when you first send data to  which url?????????you can verify form data
via in python to get form data
----
cs
---
login,regester,logout,all take actions that includes send
data to server ,server deal with data ,return html,when data sent to server will be store database or verify .
-----
someone
------
i need a heart state that when i finish all tasks,i need rest!!!!!but i face all situation is that tasks cannot be donw or i dnonot want to stop.
----
cs
---
what i understand the internet is the c/s ,sustomer
send data to server ,server detect data if need be deal with,such as user if login,if data written to database,
server's function do deal with the data and return data
to customer,from send data view,i understand what style to
be used to send data ,it related to network ,i can go on  abstarct transmit data(via internet ,forward data to corresponding function),encript data,deal data,imho ,coreesonding network and algorithm,languge.of course ,i find that you must note there is data store problem.
data problem
---
---
authication
-----
from path,i find to check a user if login in ,if not
it will stop login page--
python
---
via implement a __getitem__ and __len__ method,i can implent a sequence (or list )
most method,susch as len ,a[3],balabalbala......but i cannot change the sequece
's position  and value.imho,when you implement python __getitem__ method,when use len()
function,implecitly  invoke the __getitem__ method,other functions seem to be same!!!you must know python interpreter invoke this spicial methos,interpreter is
python version......i want to say that __repr__ and __str__ 's effect is same .but we advise you use __repr__method
imho,sequence is somthings such as animal include pepole
,monkey ,dog,pig,sequence include list.string etc
----
someone
----
i have a phonenon that i canot grasp knoledge very deeply!!!
----
python
-----
python class attribute have two type
that include 1. in  __init__ 2.in class level,but i have doubt that in class level i
 can via self.classlevelattrubute to modeify . i affirm to access is good
you can a=class(),a.classlevel to get value.you can refer to
https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
.if you can in class to implement __getitem__ method,you will a[]
and result loop and reversed .so on,you can finish iterable  function such as
for
doctest the number of item s is a problem.

---
how to install sikulix
----
https://www.youtube.com/watch?v=QiLkTP9Y_d4
use C:\SikuliX
----

encode and decode
-------
about decode and encode ,the is connetction about convert byte to objetc that human can understand.
in unicode culture ,there is a way that convert charater,it is automatic unite of  a languge, to numbers
numbers converts to bit that was storaged in computer.from now my view,unicode define a large number to
corresponding alll kinds of charater.simple to say.unicode is like a table,you can map number to charater
in the world.about ascii,i want to say if i send you 65,you understand i send a A to you.from now,byte ,asingle
byte cannot slove to represent all kinds of symbol.i need to  understand python code how to convert machnie code.

---
someone
------
i feel that i was dependent  in caton
--------
load  balance
---------
load balance represent make too many traffic to all kinds of
application server .(mr wang said).proxy server is a forwarding
request to different app server!!!
----
session and session id
-----
i understand session is paharase that  start client send request to server and server send
reply data to client between the two pharase.from my view,i think ,ssesion is to slove
the problem that how to slove http stateless  problem ,thatis,again http request ,you need to
write username and userpassword,but ssession id slove the problem,
a session id a connection.session is a data structure that
save your username and password(hassed).besides,you can save another things in
session,session connect mode is the following:user use username and
 password to login in web server if authenticated,server make a session
datastructure that includes your username and your password and allocate
a session id to the session and keep the session id in cookie and
send it to client allong with http/s response,when client go on another request,
it will send request to server with session id.
when server receive the session id .server will to check the session id if exsit
and do responding action .if exist ,go on .or server will request client
to login.  but there is another view,session a period that between user login in and
user login out.also session id and ssesion content is dictionary,eg,6374838834:{'username':yangming,
'password':xxxxxxxx(hashed)},about the form of session saved in server file system
or database or cache system.more things ,when more request were made ,you need
to send http request with session id in http body or head argments or cookie or usrl argument!!!
what i want to ask is the connection between cookie and http. another view,store too many data
in cilent-side will increse your traffic.i can use facebook  as example,when you first
login to server ,server check your passwod and username.if authenticated,fb will make
ssession id and  return your main page,and you continue request another link in your
page ,you donot need authenticate ,in the hood,the browser will use the -styile link
http://en.mail.qq.com/cgi-bin/readmail?sid=YkCUuyVilYYnMRxE,
2,en_US&rank=2&mailid=ZC3212-rI46SNYOKzg0RGk~5fHZO64&t=readsubmail&mode=fake&s=r2&base=12.07&pf=0&folderid=3&folderkey= ,you can  sid =.............
3e281772..but you need note that the session id is encrypted in cooike sent to server,but when you in chrome ,you can read uncrypted sseion id.....i want to know
when you click  a link in fb ,who make your url's sid ,who encrypt it?????more,when
clear your browser  data you will must  login again!!!!now i can undestand the connection between period and  ssession ,because after logining,your cookie will always
be invoked!!!!!!when you login out ,your sseion id can not be used!!!
----
hacker news
-----
it may does not connect to the issue by author,when thread was come up with
-----
project
------
draw a conclusion,every project need a why to use it page and
comparision to major compitor that do more good to our clients
but not damage our compeitor!!   features comparision  is important
the  project also need what is the project?????
----
nginx
-------
imho,nginx is a tool to increase web access to server to down memory and
cpu,it is similiar to apache.from some opnion .it is used to load banlance
such as ,forward all kinds of request to all kinds of app server and do more
opreation on  request,such as request size ,authen method .also another view ,
it is as a firewall ,for in a big rentepreter ,nginx act as fire wall to,for
oiur developer  cannot touch in system.
------


---
open source
-----
encrypt   
-----
english grammar
-------
Not that i donnot  welcome competition,i just donot
see a real need in this field

----
open-source
------
about open source,i get information from yc,open source lassfication
is following :game,frame ?????what i want to explore??????which type
there exists????from which drection to explore opensource?????i belive
open source hidden a mout of fortune,but where i  start?????

---
english
-----
over also present the mean of about
---
genius
----
think oppositely
think in anonoly
learn from the little and error
these view from ........
---
methodlogy
----
make anology is a sign of genius ,this view is main and  popular

future
-----
waht i wanna lean is piano
----
methodlogy
-----
use the style is good ,you can get some classfied topcs
but you need to focus on some topcs or you r enrgy will
bw be wasted!!!!
----
direction
-----
konw yourself
math
english
health
economy
computer
methoslogy
inner pysclology
.......
-----
conclusin of  it
---
from my opinon,it consiitof ,it also can  syas r&d,
version contorller,writting code,degsign frame,debug,log
,depoly(imho,that is shipping your code to production)
----
english
-----
my english spoken is poor ,i thing the reson is that i cannot
read voice accent ,what i wanna say is ponetic symbol.in 7 grade
that some resons i donnot understand ,from then,i donnot get good start
,my accent is my english confiedence shortage ,....
-----
someone
------
i find that i donnot prefer to change my derection,,,,,,,,,,,,,,,,,,,,,,,,,
sometimes,i cannot chnage ,sometime,i lack driverness!!!
it is true!!!what i say is,fuck????i onluy can use some simple
english cluase ,but it is good????


genius
-----
about genius,i read a author that may be a genius,
he said genius 's charater is to produce,in the most recently days , i
feel that my feling of years is more strong ,i feel
time is so hugrry!!!
----
qsjkasjakskaskajkasjjka
-------
economy
----
get somethings to sale higer price that is more than it's price i bought
this is a good deal
--
living
------
about living , i have sommany imagination
if i have a so luxury watch,that is so coll
if i have a so comforatable chair ,i will be
satisfied.this is iiiiiiiiiii,what is that iwant to say
these dayas, i feel so happy and sad becuase i feel sad
i met some frastrated problem that make me think myself
is stupid,but the next days , i can figure out or slove the
problem,then ,i will feel that i am good.in addition to thses
good and bad,besdes,i feel that i need a macbook for well
wrtting ,but it is necessary???i will doubt,after all,the
lennove pc work with me that make me think taht it will
work more times and my income or to say that is ti waste????
i also feel that 2016 is a good year,fuck ,i can work with english
so a year,that is awesome,in addition to i can get so important or
insight views that do help me in the living,in fact ,to sloving a
 problem ,you can open ten chrome tab ,this do more for me,
 if i have so many tech is helping me be more great man1.chrome tab
 tech 2.wirtting............what else i cannot imagne!!!!!!
----
english
----
about english .i have fellowing  puzzle ,that is ,listenning skill
and poor spoken skill and unsuffient grammar ,that is my english 's
gap that need to be filled by myself


---
prostocation
about th e psychelogy of procastion ,i wnat to say idraw a conlusin
,the viem i remenber is what you only to do is to do ,it is so scarefull
as you imagine!!1

---
future
-----
i have decide to devote my energy to math ,english ,computer,economy,problem
-sloving,if i have some fitness ,i will  get so many fortune  i thinkM

----
habit
----
inspired by someone,i get a view that he get greate succes via not wasting
his ennegy and slways get somethings,

















```


# develop
```
client send data to server and server can store data
into database or deal with the data in function
,function 's operation always ocuur in data ,

```


# master math
```
imho,math is consit of daoshu ,jifen ,alege math
,from my opinoin ,i donot get idea,that is,i cannit
get good position,this years,inned to rethink that why
form somoe pition,that i can not work hard but
i feel that i realy  work hard!

```
```
every day ,we need to get progress
just a little is a important point
```
#  client and server model
```
 ## net work  by yangming

 flask can slove all kinds of problem s
 i can abstract web develop is fellowing:
 client send  infomation to server ,server get the request
 and deal with the request ,as usaual ,it get a url .it will
 depath a url  to scratch to get all kinds of arguments.for example
 the url is http://wwww.goo.com/?queryyangming=234&ui=colorful
 .the server will get yangming and ui .after this,this argumewnts will be pass to corresponding function to deal with and get return value .
 after it,server return value send to client,and client do corresponding actions.imho,json in this course was used frequently
 as info media at http body !!!!
```


9100+129+100+100+300+450+800

[Greate acticle you need to read about wiriting and thinking ](http://www.dextronet.com/blog/accidental-genius-summary/)

# you have
```
this ia python a script

now ,i feel pride ,
because i have sloved sublime
install package problem

```
# sublime question
```
               i have sloved sdublime problelem of cannot install

                package via a stackover flow link
```
```
living is all kind s os happiness and sad
because of  sad ,happiness is chiresh

i neeed to slove sublime syntax launguge

if yesterday is sad,today is may be happy.it is so frequent
principle

i dislike limit -time in all kinds of task
it is a limit for myself
in create html page,i feel so tired in django


now,i have to activate the fellowing habit
1.make a link
2.wirtting
3................................................................
4.read
5.help others
6................................................
7.try toi answer stackoberflow problems


When you go with a thought,
you assume that the thought is true,
and you can take a series of logical steps.
 Just like this: If A is true,
 that means B is true. And if B is true, that means C is true. And if C is true,

why markdown does not work in web page paster
i copy a pagrah from web but it not work in
markdown


Secret #6: Redirect Your Attention
When you run out of things to say, you can use “focus changer”. Focus changer is a question you ask yourself on paper that requires you to comment on something you’ve just written. It keeps you moving, and helps you focus on the yet unexplored parts of a situation.

Examples of focus changers include:

What was I thinking here?
How else can I say that?
Wha

-------
someone
---------
the diffuse mode does work!!!
```
```
        def helloworld(a,b):
            print 'hello wolrd'
        if __main__=='hello':

```

# i donnot like bad document ,becuase i have word with it

   thank you ,i lovw thee markdown ,i doubt that
 corect  markdown for wirting acticle isthat
 keep correct format that no need to do morethings
 every word have been input ,this way,it is evry line is filled ,i can not affirm it is ture nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

it is ture ,via the above experiment,it is usual wirting,in these
case,you need to grasp how to control the frommat except ```````

&nbsp;&nbsp;This will appear with six space characters in front of it

链接: https://pan.baidu.com/s/1dFORYlb 密码: n3p3
```
   i belive that along the way,one can be more greate but in some
day,but i have no control my inner
yes,i am so tired in these years


-----------------------------------------

in these dayas , i beleve metholodgy can change one's life
this way,to system to do somethings and think many things
but via feeling


i can use tree command to show the structure od dir
in linux ,but i can use which tool to show these in
windows ???

```

   **[how to think via wirtting](http://www.dextronet.com/blog/accidental-genius-summary/)**


## About think
i wanna restart my think map ,but i care that i may stop
it
```
the best part of the workday is i have slove the
sublime package  install problem,it frustrate me in
yesterday,i feel sad and think i was not a good slover
of problem .even is not a  good programmer .but it
encourage me



i want to show dir tree now ,this is below via linux tree comand
          /yangmingproject/
            ├── yangminggolang
            └── yangmingpython
                  └── yangmingflask



ifeel wangwangis handsome when he is patient to answer my question
this is i feel caton's energy
--------
cs someone
----------
indie developer  
https://news.ycombinator.com/item?id=14437921

-----------------------

Prompt Your Thinking
Prompts are Freewriting exercise. When doing this exercise, you begin the Freewriting session with a pre-determined prompt.

Prompts are open-ended phrases to warm you up and to send your mind into unanticipated directions.

Prompts allow you to find many hidden jewels that you wouldn’t otherwise discover.

Some examples of prompts include:

The best part of my workday is…
Yesterday I saw a curious thing…
If I didn’t have to work, I’d…
I threw a stone and it landed…
I remember….
I’d love to learn about…
If I did the opposite of everything I normally do, my day would look like this…
I love…
I hate…
I should do more…
You know what I’d like to do again?
If I were guaranteed success, the project I’d take on would be…
The very generic ones can work wonders:

The storm
It was getting dark…
The birds were singing…
I opened the door…
Three days from now…
Prompts are somewhat similar to one of my long-time favorite techniques – question answered on paper. Basically, you write a question, and then start answering it. That’s it. It’s like querying your mind.

When you make the question very open-ended, you are not looking for specific answers, and it’s a prompt. The result will be a surprise. On the other hand, when the question is very specific, so will be the answers.




```

```
i eant to say in freewritting to that past=ing asome things
is very  stipud for aganinst it origin
```

[it  is a greate link about wiriting](http://www.dextronet.com/blog/accidental-genius-summary/)

```
may i have feel that i lack think in somethingsd because for
i lack for writting ,it is a good point
it exisit in my universty second  fresh year,i feel good  and
it is used in 9 grade  time ,i write a post about chemistry
that i feel sad about ,result i get passed in the test


i belive that hte feeling i wrete is a base to influence my judgement

but i feel it is bullshit


all i have wittren up to this point about  how to use markdown
is bullshit,the truth is that markdown is a luanguge  for writting
but a proamming language
i find that my problem is not how to slobe the problem
,my probelem is to understand problem  and understand what sloution
says .it is key to slove most problems i faces now.imho,i need to up my english ability and understanding linux basic



# using lying to eliminate error
-----
someone
-------
the fact is ,or say,i must transfer what i learn



```

#  writting can slove the problem that you can read it bbut

   you can express it later


```
python is a kind of interpreter style languge ,that is ,

it can be run after  editting code,donot need to compile

at once.it will be compile when it is running.

------------------------------------------------------

WHAT I GET FROM LEARN STYLE BOOK is following

1.writiing is good
2.make a link is good
3.try fresh things is good
4.make a anonoly  is good
5.do different things is good
6.communicate with  a  somethings

--------------------------------------------------------
what i get from 8000 hour is hte folloe=wing
1.help others is good
2.supporttive colleage is good

what i draw from life
1. money is somithings you need to do too many things


the problem i face when i slove aproblem is the following
a problem is relating to many things that i have mastered
then,i feel so tired .



linux mount is my problem.i donnot like it for in shanghai
qingsuansuo time.


i donnot  like to exact somethings becuase it is long

sometimes ,some greate opion that i undestand but i cannot convert

to my opion.this is bad




get focused on what you want !!!!!!

----
history
----
mongolia is a great contry that own most of continent
in the earth
----


```

# That i wll cherish and purse
```
1.english
2.math
3.economy
4.computer
5.isiiisiiisiisiiisisiiisiisiiisisisisisisiisisisisisiisiisisisisisiisisiisiisisiisiiisiiiissiisisiiisiiisiis
5.health,energy and love

```




# what i get from slef-controller book by stanmford writer
1.need a good blood-sugar level



```
imho,it is a good opnion to persuit somethngs and it 's others

will be  brought to you

```


# git basic

```
imho ,git or github is a repository that  save your code

git can work with github that work as repo ,make a anoly ,it

is a pool you can place  a finish in it or fetch it,you can

update your finish.






```

```
i disleike chiken soup

i love the methodlogy that can land




```
*[it may be a good link about person development](http://www.dextronet.com/blog/category/personal-development/)*

```
in a day ,if i have learn somethings ,i wili feel tired
i donnot want to learn more ,this is usual

i think i have to figure out why my sex-disre is weak ??/


```

# python

```
python for me , i have some question and era to explore
1.python thread and process
2.python asyn and syn
3.python network adn socket  programming
4.python work with c



i feel not easy of python network .it is that

network
-----------------------
abou tcp , i can undestand is a protocal to communicate
with infomation ,abou protocal i thing it is a guide that
we all referece to dothings ,tcp work in transfer layer,but
i can not understand clearly what evry layer .from now,
application layer play  a role that forward infomation ,imho,
to approtiate application,when i have to learn the widershark
too to grasp packet,the tool that give me unhappy feeling ,i
cannot  grasp .of course , i can abstract network to this sitiuation

,thst is ,a -----send infotion to-------->b ,about tcp ,i also

know its tcp three-handshake,it is all .but the shake hands course
i have forget .
--------

-----
network programming
-------
i think that  ,for example, a python flask
frame will deal with all kinds of network request,
but we need to deal with security ,productivity ,etc that
result all kinds of tech such  as sysn ,acsyn,tls.ssl .etc

----
living
-------
shanghai jiadinglibarray if have network,that is so beautiful things
i want to live in near by shanghai libray
-----------
startup
-------
idea,product,team,execution.
-----
base  konelegdeg in 2017
---------
1. master network  basic
2. linux basic comands
i feel i  ahve master python basic
# i will use -------- to block knowledge
```

# Someone

```
-------
my  innner
---------
i doubt that there is no have good quick start to a area,so i donnot
get start happy,so that i cannot go deepth!!!!!
----------
inner
----------
i feel that my disre for  back chengdu is get more strong..
is it sigin that i can not work hard,or i can not be used to
hard mode??????
-----
someone
--------
why my heart is not so stable??sometimes,i can persist/want a things to do to the end
and the time i donot want to start another thing.but sometimes ,i open/start so many thread things ????but not to succedd finish.i feel so tired....
------
someone
-------
from now view,i want to get things ,so,this things will  occur ,
for example,i want to understand
how python excute a  .py ,
and the internet and youtube give me how to implement a interpreter.
------
someone
-------
is it so strange to communicate with a  stranger.
-----
cs
-------
i need a app run in ios/andriod to send instructions to upload my daily news.
------
someone
-------
i think that i need to read a set of source code to leverage my knowledge
--------
someone
-------
what is that  i wnt to say?so the result of  many things donot behave similarly to  you imagine.
------
someone
-------
in fact,in the real living.i feel that my mood state have flawed space.
such as,i cannnot endure ,or say.i cannot receive someone around me behavior
well than me ,even if the fact is so.i always think that it is temporary.
the character of donot obey discipline/ always results too many troubles.
-------
someone
-------
i surely need to rethink why i can not finish a things at onece.
in the recent days,my task progress is so slow.
------
someone
--------
it seem that the encyclopaedia britannical is very spicial book.for it always
was mentioned in all kinds of situation.
------
someone python freewirtting
---------
so i set a note book in ipython set a  alias ,that is forever,
to quickly edit my freewritting txt.
------
someone
-------
try to develop the ability of excute somethings.this is important.
-------
someone
-------
i can not find a way to convert my knowledge to pratical applicaton.
------
SOMEONE
-------
what you think you will get is always not same with wht you get finally.
-------
someone
-------
i must admmit that the desire of learning is weak,i need to rethink that
the problem-driven learn.so i may have not skill to slove all kinds of tests.
--------
------
someone
-------
i think that i am always look for great chance.so that
i cannot work seriously.
--------
someone
--------
i cannot inmediately to do the things i donot like.!!!!
---------
future
---------
fast company may be the source of starup
--------
someone
----------
i must cherish the power of habit.
--------
someone
--------
try to combine education and game!!!!
--------
someone future
-------------
set english listenning exercise program.
-------
someone
---------
i must make use of all kinds of experience comapny with
all kinds of reality.such as side project .
-------
someone
-------
so,i donnot feel my energy or the disre of exploration.
-------
fd
-------
when i finish a dream,i feel it is  so normal.real!!!so i doubt that it is not to waste too much energy.
---------
someone
------
from some situation.i need to learn english grammar and english vocbulary.i feel so hard to
scan the hackernews.
--------
someone
---------
i dislike configure


--------
someone
--------
i find that github is a very good place to slove a problem



--------
SOMEONE CS
---------
i feel that again  i need to learn the js gramamr


-------
someone
--------
i find that when i get in trouble,the stack over flow donot have good
solution,when i slove the problem .ican deal with the problem and give
solution


-------
https://www.youtube.com/watch?v=3xQTJi2tqgk
---------
someone
--------
i feel that in caton i have a fear to ask others problem

------
someone
--------
i find that when i think ,i cannot leave a pen to
think so spicial rigorous probme
---------
someone
---------
i can use the scientfic method to standard the things i have learned
or say.i can make use of cs to develop the productivity and
cultivate habits
-------
someone
--------
i need to change the strategy to recite words ,that is,
firstly ,to affirm which words is these words i canot understand



---
someone
-------
my middle scholl time ,i have a habit to writting,but then,i have no
view on wirtting,i find  that in many point,you can be a genius,but
after later.you will give up for all kinds resons and fact...
---
someone
-----
about fudan ,when i know fudan have receive me ,i want to share the info.is this vain???
this situation happen to many times,so ....someone doesnot like me.
-----
----
someone
-------
i can remember ,i buy so may books and watch so many  movies or download
so many material,but ther life is so short.my interrest will quickly low down.
--------
someone
------
i canot staty in my comfort zone,i know this things,but
i fuck my comfort zone ,it is so painful!!
-------
someone
----
in chirldhodd,i use yumi stem to build somethings ,imho,that is
a sign to reavel my character to create somethings,that is onnect
to the view (what is a ginus)  
---
about health
-------
to increase blood-sugur level is a good method to keep control yourslef
and i feel worried about my health ,is following1,my weigh is ,is
it importtant???????my sex desire is not so high that i have no confidence
to seek a girl ......i doubt that wheather my  kidney work well.or my  maturbation
is so frequent so that ?????these years my weigh and my body-form is not satisfy
myself.but form other hands,my body donot get bad sick ,it is magic or luckily!
i need some info to change my health about sex disire ,tire,body-form....


-----
someone
------
i find that i will doubt this world,i am willing to believe
the world that i belelive ,even if the research guide by the
top agency and famous reseacher 1！！！！！

----
-----
someone
-----
about distraction.my solution is that place my time in a bucket that
including math,cs,english,and economy.that will do well,i guess,but
there are a problem that how can i can i orginize the konedege that
i donot drown in the ocean of konelege????
----
someone
-----
i feel like that my the shit problem is stop a things in half way
many things i donot perserve anfd i cannot go on,why?this is
my biggest problem.
-------
-------
someone
---------
at some point,from my view,the bad or pain feeling of  start  a things
will dispear when you start to do the thing!!!!
----
----
someone
----
i remember that when i was in middle shcool.i hope that i casn quickly gradute from school
that i can do more things ,but from now situation. i donot think the deisre of past time is good.
i just want to say ,you should cherish the presenting time.
----
someone
-----
i have so many great ideal.but for all kinds of resons ,all these fail.
----
someone
-------
i can not finsd my passion ,why,so ????

------
-------
someone
---------
i believe the tech is becomming,which tech can forever exsists.???
this is the reason that i want  to enter spicial realm.
--------
someone
---------
i think that the game,ai,.........where i can get that directon i want to start?7
-----
someone
-------
i thin that i need to audit every paln ,that is,how to start ,when to start,when to finish
,via my ability i can set a conutdown timer for my plan
-----
someone
-------
i must increse the ability of deal with all kinds of pratical problem.or
i will lost confidence of deal with all kinds of problem
-------
english and somone
--------
i find that when i meet a problem,that may fuck my comfort zone ,i may lost
patience.such as the ugly doc.
-------
someone
------
i also need to rethink that until today.i cannot grasp a set of open source technology
.this is so dangerous for me!i think that it will damage my enthusiam for tech.so that
i think the tech is the world i now imagine.
-----
someone
-------
i musa rethink that  in the living,do i open too many thread so
that i canot deal with it properly.
------
someone
-------
in the middle school.i try many methods to increase my interest/desire to learn all kinds of
subjects,why all these methods does not work???/such as, i wanna put the index of problem to bottle and
randomly pick a number to slove.i doubt that i donot get the essence of learning/interesting.
-----
someone
-------
when i read the book ,that is, master complixity of science and enginerring ,i have no desire to read
continuely.
someone
-------
how to build  a robot that can behave like a man or   cat.
-----
someone
-------
my inner state make me not study from others,i feel the state
having exsit many years.
----

-----
someone
------
why i have no desire to forward.????so ?do i need to find a direction.besides.from the past experience,i think that the money can bring funny  to
me.
someone
------
i rethink that  if you want to a things successfully .you need to build self-principal,good habit.and you need to try to rethink more !
------

------
someone
-------
i think that i need to know what is my advantage ?????

----- someone --------- i believe that i need to restruct my ability about
doing a things ,descipline, ----- someone ------- i feel that my innner is
worring about ,i was disrupted. ------ someone ----- i believe that i have bot
find the goood learning method for me,my middle shcool and  graduate school
test is a good example for me ,that denote that ,but i donot  think the
problem cautionfully ------- someone -------- when a thing was not finished
,espicially  a very important things,such as fudan advisor  confirm mail.i
feel the worry of my inner . ------ someone ------- masturbation........

-----
------
someone
-------
i feel that recently i donot be trusted by caton's nomal people!
-----
someone
------
many things, i believe that may it be ,i know the result ,but i cannot  adjust the
result ,when i do some things , i always struggle to repeat the old methods.besides,i do many things according to my  feeling.
-----
someone
-------
i need to listen these things others fuck their comfort zone.


------
someone
-------
i have find that some one 's view donot let me feel softly!!!!!i need to
absorb all people's view.
------
why
-----
why the world is so many genius ,but am not  i ???
------
someone
------
i findthat china have so many chance in web innovation.
but i canot do more encourage step.
----
SOMEONE
------
so long,i donot find a beautiful song.
----
someone
----
i remember that i may think future 'day,if i want do what i think,the future it will be what i think ,this things is  so much.


-----
someone
-----
i feel so tired in the next day after masturbation.

---
someone
------
why i cannot start important things  in a day?these years.
------
------
someone
--------
i want to look for a way to improve and level up my pythotn tech
but in the one of three of march ,ialmost switch all kinds of python books,
i  donnot get suitable python books,i may need to rethink  mrs wang 's
problem-driven to learn.'
and i want to set up  a company to host my calender and to do list app 's disre
is having bee n so strong.!!!!'
-----


------
someone
-------
i feel that i need a girlfriend.so ,may it be.i feel that i am so crowded in my inner.





-----
i understand why my  web have no advance ,from my view, ihave no a suit for me  database that is free.i beeleive database i have solution that is i use weatherapp send data to tencent database!!!
!!!
------
someone
-------
may it be ,my middle school time is destroyed by my eye.

-----
someone
-------
these years, i can not be likeed by many.this is my character.
someone
-----
now , my willing is to be expert in mysql and python.!!!before may
----

-------
someone
--------
i need to think my productivity of daywork.i have no room to think  from this view.
-------
someone
-------
i find that the poor is the reason of all kinds of problem.
i doubt that my communicatr skill have faulty.besides.lack of money
lead that  i canot deal with all kinds things .so i find that
i have no consciousness so that many money canot be make full use
so that i waste so many money ,when i get money ,i usually
waste many money in the first period.
----
someone
-------
when  asomeone doutui ,he feel so happy?

-----
someone
-------
i understand my disre of  create a simple appp  ,for
i  think i may  not hold or say, i have no so many energy
to do  more complix things.
---
someoene
------
once i believe that i need a clean body and bed room  and cup
,if own these things ,i will be satisfied.i donot need to worry about my next food and next shoes and so on.
----
someone3
--------
i will  adopt just a littlite  advance ,i believe this method is healthy
!!!!

someone ------ may it be.making a decision is difficult.it will cost
willpower. --- smeone ------ when i finish a things, i donot want to start
another thing.such as when i was admitted to fudan. i donot like write any
code during mar.

--------
someone
--------
i find myself for work i have so short time to like it .when i enter the stage
,i donot will go on it .i feel so sad.
--------
someone
---------
i need to merge my cs to geo metrio.
------
someone
------
i feel that i have no desire to work  from past to now,is body weak??
--------
someone
-------
i  know the embrassment of fail is usual ,such as a beautiful girl ,i dare not to
say to her.
-----
-----
someone
-------
i doubt that i have no a very strong body so that i cannot work well ,but i also
doubt that for i allways stay up so that my body was influenced
-----
someone
-------
i guess that in the chirldhood ,the resource of fun is rare,so we feel happy.now.so many things  can stimulate our feeling,so our feeling is cabbin
someone
-------
i think that if i am the road to the destination ,i will get progress.such as ,i think that i read hacker news,my english will get awesome progress,so my ability of reading english will get upvoted .so when i read the complexity of science and engerniring will be so easy.
------
-----
someone
-=----
i have find that i have no desire to find  the  great  solution for i have no desire to work.
----
someone
-----
i find that when i slove a probem ,when it related to many things
i will be distracted,so may be my cause for can not finish a
things totaly ,it may be that forget why start?????
----
someone
-----
i wanna listen other and i wanna cultivate the habit that make me
do one thing at once.
----
someone
------
the drawback that i cannot learn from others is main factor contibuting to my  
all kinds of failture.
------
someone
-----
when i have carros primary or /start stage ,i havenot get more progress.
------
someone
------
poor and lazy is so bad feeling,my abbility of eye is rapidly down .
-----
------
someone
-------
i have a trend that i believe opinion by i believe he is a great pepole
------
----
someone
-----
i used to repeat myself in diffcult or complix problem.
-----
someone
-------
once i grasped code , i can use top reascher agency's
paper to develop my ability and bussiness!!!
------
someone
-------
chance is great , i can get somethings from paper from
top university.this is great!!i believe my fortune will from there.i can use machnie to help my english spoken.
i can make appp  that every one can send a luanguge to the server and the server will response a native language to help language leaner.
-----
someone
-------
whatever.i admit that money is very impotant.but i can not change my mood.
------
someone
------
did i have the request myself to learning according to prob;em.besides,i need to
note that i donnot  grasp the problem deeply.such as ,when i am in fudan ,interview with  mr tang .when the teacher ask me the difference bwtween thread
and program ,i feel so ashamed !!!!these problem i met many times,but i have no
ideal ,the situation occured ,such as interview with fd gradute,when he ask me that the vm mode i donot have the disire to look up ,but the later days,he again ask me the problem.s  

------
someone
-------
i donnot like to implement these things ,is it because i lack the desire to dissect
 these things.!!!
------
someone
-------
in the future, i think there will be more failure and more sadneess.i hope myself
for my future i have a good state to deal with.
----
someone
-------
i doubt that i  can only do just a little of  a big task .for ,so,i have motivation to do
it ,but i remember that this go against the ted experienece ,this is,you never have
desire to do a thing.





------
someone
--------
from some view,i have no good rest to lead to my bad status of today!!
-----
someone
------
recents days.i draw a lesson,even
----
someone
------
so ,i think that in many time ,i donot know the others' feeling.i just think in yangming's view
------
someone
-------
many things ,when it occur.you will doubt that this is not you imagine ,such as fd tangyuan test.
i thought i will compete over any  obstacle about the test teacher tang give
------
someone
-------
i have find that when i am in interview,i will lost logic ,espicially ,i want get /win the job.or
i get negative info such as from advisor ,he say are you sure!
-------
someone
-------
in the interview and test ,i always lost logical and forget i have mastered ,such as matrix ,tangyuan

-----
someone
-------
i need to worry about my body,i cannot prevent my
the tire of my body.
-----
someone
-------
i should remember everythings the i get anytime.accroding to a mind for numbers
and others.of course.it also mentioned in all kinds of stuff.
-----
someone
---------
i must admit the fact that the result differ the things you want
-------
someone
--------
sometime ,i want to show myslef to someone.but
i have no encourage to show myself to others
who seem to be more strong than me
------
someone
--------
sometimes,i have so many words to speak to others
-------
somone
---------
i find that when i am debating,i can ask the one that what is your problem?
-----
someone
-------
lack confidence for the two year of middle shcool.i cann not  justify the state


-----
someone
------
i have finfd that the key importance of  habit
-------
someone
------
i must rethink that these years,why i have no a love girl accompnay with me ???



-----
someone
-------
i must face the fact that i lack confidence.i feel that

-----
someone
----
i need a  job to slove the crisis of my living


--------
someone
--------
i find that i have try many time to develop my english ability such as i in middle school
,i wnt to read english novel to achieve the goal.


-----
someone
--------
i find that when i  am face some real things ,i need great courage ,when you imagine it ,you may simplify
it
------
someone
-------
i have a geuss that since my liveing is becoming
-------
someone
-------
when tangyuan ask me some problem about matrix,i feel that i can slove it with pen but via brain to imagine
i feel so hard!!!!                              
------
someone
-----
i find that i have no habit to repeat .i dislike repeat.so many things.if  i
donnot like these things,why i need to push myself.for a colorful future.?

---------
how to write video files to dvd
-----------
https://www.youtube.com/watch?v=4v3M-yTZufs






-------
someone
-------
i believe that when tangyuan ask me do you think your programming skill is proficient.i say no
why i donot reply if it is python .i bet that i will do anything.whatever,the fudan teacher give mw
too much think and ideal.
----
someone
-------
in middle scholl. i always do things that i want to do ,i donot obey the teacher instruction since
i think that the ability of my teacher is not sufficient!

someone
-------
i think i need to restructed  my view to end
develop and it, i feel my knoledge is not sufficent
to develop my career.
-----
someone
-------
i donnot know the reason that i dislike all kinds of deadline!
-------
someone
--------
about problem-driven .i find how to find a problem ,it is a key important problem.
--------
someone
-------
i find that i always expect too much for somethings i want
------
1.use iso file and install windows https://www.youtube.com/watch?v=o8I600ToTOQ
1.fix windows can not be install to disk https://www.youtube.com/watch?v=DQf9YqbD8WI&list=LLbSoUzZ6Uv5GL7vCDYa6s2Q&index=1
2.use qudongjingling to install network card
3.partiate disk https://www.youtube.com/watch?v=q6_wwuBp0iI
-------------
someone   estate
-------------
i can search make money from hacker news to get insight  and inspiration from hacker news
-----
someone cs
-----------
hacker news is a good idea.also a great web where you can get insight and inspiration

---------
someone
-------
i find that samba server setting is painful for me
-------
someone
------
when i masturbation,i fell acid in my back
---------
someone
-------
when someone  give gift others but me.i will feel wired feeling,is it Jealousy??????
-----
someone
--------
when i get just a little porn info,i will get invovled in pornhub.
---------
someone
--------
i find that when i liaten oethers' judgement of myself, i will  be angry very long time or remenber the things that will impact my mood very longt time.
-----
someone
-------
the sentence .that is,fuck your comfort zone ,is said easy,but when you do it ,it is very difficult to do
when you fuck your comfort zone,you will feel very painful.

-----
soeone
------
in the past,i think when i grasp the basic of writeing code ,i can too many things.now i
have node disire to do anythings?
-----
someone
-------
i can not persist a thing .
Is it because people are greener?
--------
stack overflow business mode
----------
https://stackoverflow.blog/2016/11/15/how-we-make-money-at-stack-overflow-2016-edition/
-----
someone
--------
people behavior
people psychology
people negotiation
game theory
math for cs
economy
english
-----
someone
--------
i have download all videos i need ,but i  have hasitates to start,why?so long time past.
-----
someone
-------
the ability of sloving probelem is about think more or willingly
such as stanfordbehavior subtitle,if you do this things manually.
the things also can be done but the producity is very slow.but when you
try to use python to slove the problem .you will feel the pleasuer and
what you may donot feel.
------
someone
--------
i find that the study about three things,english,math,and the stablity of habit.
so ,i doubt that learn psychology is great way!
-------
someone
--------
i need to rethink what happen in the time of middle school?why lead to my bad
study score.i doubt that i donot have to sink my heart to study,but my mood
was lead to great goal just care about fudan,when you sink your heart to a thing.
besides,i must care about the enviroment then,such as  lack money ,such as a bad
study env (bad relationship with colleges),besides,my character cannot keep touch with
or loved by everyone.why my middle school is very bad!!!!!!!!
i also remenber that when i understand somethings,i always donot grasp the esentials
in dongchen,such as,bio,or chemistry.from now view.i think that i lack effective repeation
and then i have no mood to understand ,i feel so anxiety in dongchen.i think it is awkward
for me,so my mood donnot sink in study.i think ,the mood is very important.
----------
-------
someone
------
i need to figure out,why i have no girl friends?
recent years ,i think that i think that i darenot  fuck my comfort zone.
------
someone
--------
i must be aware of my body.i worry that my penis cannot work with my girls.
besides,i worry that my body ,in some condition,i may lost eneny to battle.
-------
someone
--------
discipline is a very important domain for me.if i lack discipline.i will progress slowly.
---------
someone
-------
fuck your comfort zone and discipline.this is main domain i need to take efort.besides
you canot do any ineleegal things.besides.i may forgive my past
-----
someone
-------
may it be,i need to learn how to song.
---------
---------
someone cs
-----------
shoukd reforce my regular expression
--------
someone
---------
i need to read the power of habit!
-------
someone
---------
i find my character will be diffcult to communicate with others
may it be.it will influence the communication with others


-------
someone tech
---------
will you think tech will change the abrupt social problem?
---------
someone
-----------
how does tech change the society and china?
---------
someone
----------
so maybe,i should combie my skill with the society!
-------
someone
--------
i should write a libray include python connect mysql.
------
someone
------
i need to think that i  need to retthink my plan of every day.besides,i need to rethink that
why can not i sink my heart to anything,of course,i said so.it may not be accurate.but
you need to notice the things.
someone
-------
is it my stargery have problem
try to change single video download strage.
--------
someone
-------
i need to understand the underhook of  recognization,that is,python automatical.
------
someone
--------
i want  to make money from my side-project .
-----
someone
----------
learn by problem.that is very important.but ,i want to say .driven by problem,you may
lack imagination.for example.?????
------
someone
-------
is there ,i have a need to study how to date girls?
--------
```


# python
```
---
python
----
imho,python is simpile ,python use list ,dictionary,set
as basic datatype ,in other worlds ,i just am familiar with these,
i understand python decorator is a packager that package gift
but gift does not chnage .origin function allso all ulity
,but origin function need to have have return value ,the return
value will be used to make somthings.for example ,i write a decorater
function to print decorated function got arguments.i think that
youtube and twitter or internet have good resource to help
you become more great pythoner .python also have a view,that is,
your code is pythonic..........from where i stand,i find that if you
can not make use of anonoly to compare .after this time,you will forgrt
what you have understand........
python
------
python all object was inplemented by class ideal by doctor zhang
-----
python
-----
python interpreter run  a .py file located in disk and ask os to allocate space in
memory to run the program.before compiling,there is a paser ,it will parser grammar
to syntax tree,comiple the tree to bytecode.there  are more discuss,in compile,that is
,.py------>.pyc that is,in fact,import sector will convert to .pyc .for example.a.by
include import b(b.py),that is ,b.py-------b.pyc.but a will not compile.but in the runtime a.py will be compile to .pyc in memory.........but when you exit ,it will
delete .pyc file..
-----
python
------
form now,i feel that python all kinds of methods implemented by class method
aalso,class method main include magical method,this is main method to implement
such as len(), d[k],in so on .yeah .of course,i doubt that string ,list ,dict is
some subclass ,just  a guess ,such as ,collection,object .......balbala.about class method ,there is a mechinism called fall back to ,it is, when you invoke a method ,the method doesnot exist ,it will invoke another method.
------
python
-------
python array 's exsistence let me feel annonyed ,bacause
my c foudation is weak.
------  
python
---------------------
i feel that python 's diffcult part is
python generaor ,python work with c,python network
python iterator ,python decorator
------
python tech stack
-------
Qualifications: •Familiarity with our technology stack:
Python, Django, PostgreSQL, Nginx, Varnish,
 Redis, JavaScript, Angular and Bootstrap –
 all on Linux on a popular public IaaS or PaaS.
  •Experience working in DevOps environments.
  •Understanding of security standards and concepts.
-----
-----
python
-----
from yangming's view ,when you use a=5 or b='yangmingishandosmor',when you run python
python will allocate memory according to size,besides,'yangmingishandsome' is convert to
byte according to  utf-8 encoding schema.i want to ask who  finish the encode ,is python ??
is the gcc???
-----
english
------
that syas,
-----
living
-----
in your wall ,use 8 or 10 group swithc ,your ligth world is beatiful



```



# cs
```
------
algorithm
--------
i understand algorithm is about :sort ,search,heap,queqe,stack,link list,graph,my view is form
yanweimin,i can remember sort is very importtant ,sort algorithm has so many types:bubble sort,
bucket sort,heap sort ,iterate sort,or so on, i canot remember ,bubble sort 's principle is very simple,in ervery iteration,you need  to make the corresponding element to correct position.if there is 1,3,4,2,5'
for 5>2,you left position ,for 2<4,2 will be in 4  origin postion ,for 2<3,2 will  be in 3's position ,for
2>1, i will go 1,i 's left position has no number .first sort is ok!!!!!iin algorithm ,i dislike complixity
analysis.for i feel that i cannot grasp math and logic in these algorithm.i believe 5,4,3,2,1 is the
shit  case of bubble sort.this is o(n*n)! i remember there is another and usual sort algorithm............
------
cs
------
stanford machine learning is recomend very proundl!
-----
cs
------
i believe that the core of cs id math and algorithm ,if i have a good understand of math and algo.i will
beat all kinds of coder.
-----
cs
-----
stanford open so many course that lead to very influence
------
when we are change the old education.we can change the triditional education in  remote education?
------
cs
-------
stanford  database is very good!!!!!
-----
cs science
--------
My advice to self-learners is: never engage in "cargo-cult programming". This means: do not touch or reuse code that you do not understand. Force yourself to understand. If you lack the time, write it down and follow up later
-------
cs computer vision
------
let the computer to understand version ,you need to
input so many immages to train the neural network and the algorithm
will be smart .it will recognize the graph
https://www.youtube.com/watch?v=40riCqvRoMs


---------
course
---------
http://academictorrents.com/

```

# economy

```

















inbox=testdatabaseinbox=yangming+is+hereinbox=feel+like+mother+poorinbox=try+to+use+the+tag