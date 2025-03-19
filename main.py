from flet import *
import os
import requests


def current_year_is_2025():
    year_2025=2025
    current_year=None
    test=0
    error=''
    try :
        r = requests.get('http://just-the-time.appspot.com/')
        #2025-03-19
        current_year=int(str(r.content.decode().strip()).split('-')[0])
        if current_year!=year_2025 :
            error="This year is not 2025."
            print(current_year)
        else :
            test=1
            error="It will be Activated."
    except Exception as e:
        if "Failed to establish a new connection" in str(e) :
            error='The phone is not connected to the internet.'

    return test,error






class ACTIVATION:
    def __init__(self):
        pass
        

    def g(self,X):
        M=[[6, 4, 0, 5, 8, 1, 9, 2, 7, 3],
           [7, 0, 2, 6, 5, 4, 3, 9, 8, 1],
           [1, 6, 7, 9, 0, 5, 8, 3, 2, 4],
           [5, 6, 9, 8, 7, 1, 4, 0, 2, 3],
           [7, 6, 4, 3, 8, 1, 5, 2, 9, 0],
           [1, 9, 0, 5, 4, 8, 2, 7, 6, 3],
           [0, 5, 8, 2, 3, 7, 9, 6, 4, 1],
           [3, 0, 8, 2, 4, 7, 1, 9, 6, 5],
           [8, 9, 7, 3, 4, 6, 1, 2, 0, 5],
           [1, 0, 7, 3, 8, 5, 4, 2, 9, 6]]

        Y=[]

        for i in range(10):
            s=0
            for j in range(10):
                s=(s*3+7)+M[i][j]*X[j]
            s=s%10
            Y.append(s)
        return Y


    

    def create_activation(self,date_creation_as_serial):
        #print(date_creation_as_serial)
        #remove '-' and ' '  and '\n'  from date_creation_as_serial
        date_creation_as_serial=str(date_creation_as_serial)
        
        date_creation_as_serial=date_creation_as_serial.replace("\n","").replace("-","").replace(" ","")

        X=[]

        for e in str(date_creation_as_serial) :
            #print(e)
            X.append(int(e))
        #print(X)
        Y=self.g(X)
        for i in range(5):
            Y=self.g(X)
        activation=""
        for e in Y:
            activation+=str(e)
        act=activation
        CHAR="-"
        act=act[:2]+CHAR+act[2:4]+CHAR+act[4:6]+CHAR+act[6:8]+CHAR+act[8:10]
        return act
    
    
    
    

    
    def get_date_cretaion_assets_as_serial_number(self):
        #hada howa li kankhdm bih bhal serial number
        #had ra9m li kitla3 howa mo3arif lhatif howa likhas nswabo bih taf3il
        ti_c = str(os.path.getctime(ASSETS))
        date_creation_as_serial=int(str(ti_c.split(".")[0])[-8:]+str(ti_c.split(".")[1])[:2])
        #print(date_creation_as_serial)
        #round date_creation_as_serial bach mayb9awch ki tchabho
        X=[]
        for e in str(date_creation_as_serial) :
            X.append(int(e))
        Y=self.g(X)
        new_date_creation_as_serial=""
        for e in Y :
            new_date_creation_as_serial+=str(e)
        return  new_date_creation_as_serial



    def check_activation(self):
        test=0
        key_activation_supposed=""
        try :
            #open txt file activation.txt
            #read file
            f=open(DIR_FILE_ACTIVATION,'r')
            s=f.readlines()
            f.close()

            #remove '-' and ' '  and '\n'  from key
            key_activation_supposed=s[0].replace("\n","").replace("-","").replace(" ","")
            
        except :
            f=open(DIR_FILE_ACTIVATION,'w')
            f.close()
            pass 

        

        #
        date_creation_as_serial=self.get_date_cretaion_assets_as_serial_number()
        true_activation=self.create_activation(date_creation_as_serial)

        #
        #print("true_activation : ",true_activation)
        #print("key_activation_supposed : ",key_activation_supposed)

        #remove '-' and ' '  and '\n'  from  true_activation  and from key_activation_supposed
        
        true_activation=true_activation.replace("\n","").replace("-","").replace(" ","")
        key_activation_supposed=key_activation_supposed.replace("\n","").replace("-","").replace(" ","")
        if  key_activation_supposed==true_activation :
            test=1

        return test









#ACTIVATION
ACT=ACTIVATION()

ASSETS="assets//"
os.makedirs(ASSETS,exist_ok=1)
SIZE_TEXT=30
H_BUTTON_BACK=40
SIZE_TEXT_NUMBER_QUESTION=18
DIR_FILE_ACTIVATION=ASSETS+"activation.txt"
DIR_FILE_ANSEWER_AND_INFOS=ASSETS+"answer_and_info.txt"
DIR_FILE_TRUE_ANSWER=ASSETS+"true_answer.txt"
DIR_FILE_NUMBER_SERIE=ASSETS+"number_serie.txt"
DIR_FILE_NUMBER_QUESTION=ASSETS+"number_question.txt"
FILE_CHECK_STABILITY_SERIAL_NUMBER=ASSETS+"stablity.txt"
TXT_ANSWER=""
TXT_TRUE_ANSWER=""

B_CORRECTION_CLICKED=None

I_AM_WAS_IN_CORRACTION=0

DIC_ANSWER={"1":"0"  ,   "2":"1",   "3":"2"  ,  "4":"3"

            ,"1-2":"5"  ,   "1-3":"6"   ,  "1-4":"7" 

            ,"2-3":"8"  ,  "2-4":"9"

            ,  "3-4":"A"

            ,  "1-2-3":"B" ,  "1-2-4":"C" ,  "1-3-4":"D" ,  "2-3-4":"E"

            ,   "1-2-3-4":"F"
            , "":"-","-":"-"}

DIC_ANSWER_INV = dict(map(reversed, DIC_ANSWER.items()))


#check activation
VAR_ACTIVATION=ACT.check_activation()



def get_number_total_of_series():
    _number_serie_total=0
    try :
        f=open(DIR_FILE_TRUE_ANSWER,'r')
        s=f.readlines()
        f.close()
        for line in s :
            if "#" in line :
                _number_serie_total+=1
    except :
        pass

    return _number_serie_total


    
def write_answer_on_txt_file(n,answer):
    """n=str(n)
    if ".txt" not in n:
        dir_file_question=n+".txt"
    else :
        dir_file_question=n
    """
    #read txt file
    f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
    s=f.readlines()
    f.close()

    print(s)

    #replace answer of questioon number n
    new_answer=f"{n}:{answer}\n"
    s[int(n)]=new_answer
    

    #writeslines
    f=open(DIR_FILE_ANSEWER_AND_INFOS,"w")
    f.writelines(s)
    f.close()
    
    
        

def organizeAnswer(answer):
        answer_organiser=''
        answer=answer.replace(" ","")
        l=answer.split("-")
        while "" in l:
            l.remove("")
        for i in range(1,5):
            if str(i) in l:
                answer_organiser+=f"{i}-"
        answer_organiser=answer_organiser[:-1]
        if answer_organiser=="":
            answer_organiser="-"
        return answer_organiser

    

def on_click_principal(e,list_Buttons,text_answer,page,number_question):
        print("on_click_principal")#rja3
        #val = e.control.text
        val=e.control.content.value
        index=int(val)-1
        print("val  :: ",val)
        B=list_Buttons[index]

        old_color=B.bgcolor

        if  old_color=="#ff585d" :
            new_color="blue"
        if  old_color=="blue" :
            new_color="#ff585d"    #ff585d    
            
        B.bgcolor=new_color 
        

        #generate answer
        answer=""
        for B  in list_Buttons  :
            if  B.bgcolor=="blue" :
                txt_B=B.content.value
                print(txt_B)
                answer+=str(txt_B)+"-"
        new_answer=organizeAnswer(answer)
        print(new_answer)

        

        #
        
        #answer_writed=
        
        write_answer_on_txt_file(number_question ,new_answer)

        #update text_answer
        #print(text_answer)
        text_answer.content.value=new_answer

        
        

        page.update()
        
        #print(old_color)

        







def check_stability_serial_number():
        current_serial_number=str(ACT.get_date_cretaion_assets_as_serial_number())
        txt_content_arabic="أغلق التطبيق و قم بإعادة تشغيله حتى يظهر معرف الهاتف. قد تقوم بهذه 4 مرات كحد أقصى"
        txt_content_english="Close the app and restart it until the phone ID appears. You can do this up to 4 times at most."
        txt_content=txt_content_arabic+"\n"+txt_content_english
        #f"{serial_number} : تعريف الهاتف "
        
        test=0
        

        if  os.path.isfile(FILE_CHECK_STABILITY_SERIAL_NUMBER) :
            print('os.path.isfile(FILE_CHECK_STABILITY_SERIAL_NUMBER)')
            #ila kan sir 9rah w jbd mno serial number w 9arno b had ltkhd jdid
            f=open(FILE_CHECK_STABILITY_SERIAL_NUMBER,'r')
            serial_number_read_from_file=f.read()
            f.close()

            #remove '-',' ' ,'\n'
            serial_number_read_from_file=serial_number_read_from_file.replace(' ','').replace('\n','').replace('-','')
            current_serial_number=current_serial_number.replace(' ','').replace('\n','').replace('-','')

            print(serial_number_read_from_file,current_serial_number)
            #comparer
            if  current_serial_number==serial_number_read_from_file:
                txt_content=f"ID Phone : {current_serial_number}  "
                test=1
            else :
                f=open(FILE_CHECK_STABILITY_SERIAL_NUMBER,'w')
                f.write(current_serial_number)
                f.close()
                
        else :
            #ila makach had l file creer w ktb fih serial number serial_number
            f=open(FILE_CHECK_STABILITY_SERIAL_NUMBER,'w')
            f.write(current_serial_number)
            f.close()
        return test,txt_content



#hada dial bach t verifier wach t satbilisa serial number (li how date de creation de 'assets')
#ola mzl
VAR_CKECK_SATBILITY,TEXT_CONTENT=check_stability_serial_number()






def main(page:Page):

    #functions
    def changeNumberSeire(e):
        new_serie = e.control.text
        go_to_serie(new_serie)

    def go_to_serie(new_serie):
        #page.appbar.bgcolor="blue"
        #page.appbar.title=new_serie  page.appbar.title={'value': '1- السلسة', 'n': 'title'}
        page.appbar.title=Text(new_serie)#['value']=new_serie


        #update correction if i am in correction
        if row_result_back.visible :
                    go_to_correction()

        #save number serie in txt file
        n=new_serie.split("-")[0]
        if "س" in  n :
            n=new_serie.split("-")[1]
        
        write_number_serie(int(n))
        page.update()

    def changeNumberQuestion(e):
        new_number_question = e.control.text
        #page.appbar.bgcolor="blue"
        #page.appbar.title=new_serie  page.appbar.title={'value': '1- السلسة', 'n': 'title'}
        #page.appbar.title=Text(new_serie)#['value']=new_serie
        #page.update()
        print(new_number_question)
        

    #on_click_1
    def on_click(e):
        if VAR_ACTIVATION:
            number_question=int(B_number_question.content.value.split("-")[1])
            on_click_principal(e,list_Buttons,text_answer,page,number_question)
        else :
            show_alerte_activation()

    def on_click_on_button_correction(e):
        global B_CORRECTION_CLICKED ,  TXT_ANSWER,TXT_TRUE_ANSWER
        #n=int(e.control.text)
        n=int(e.control.content.value)
        
        
        if not  B_CORRECTION_CLICKED==None :
            i=int(B_CORRECTION_CLICKED.content.value)-1
            #print("TXT_ANSWER[i:i+1],TXT_TRUE_ANSWER[i:i+1] ",TXT_ANSWER[i:i+1],TXT_TRUE_ANSWER[i:i+1])
            if TXT_ANSWER[i:i+1]==TXT_TRUE_ANSWER[i:i+1]:
                B_CORRECTION_CLICKED.bgcolor='green'
            else :
                B_CORRECTION_CLICKED.bgcolor="red"
        
        #go_to_correction()

        B_CORRECTION_CLICKED=list_all_buttons_corrections[n-1]
        B_CORRECTION_CLICKED.bgcolor='blue'
        #write answer
        i=n-1
        text_answer_candidat_in_correction.text=f"{DIC_ANSWER_INV[TXT_ANSWER[i:i+1]]}"+" : "+" الاجوبة "
        text_true_answer_in_correction.text=f"{DIC_ANSWER_INV[TXT_TRUE_ANSWER[i:i+1]]}"+" : "+" التصحيح "
        if TXT_ANSWER[i:i+1]==TXT_TRUE_ANSWER[i:i+1]:
            text_answer_candidat_in_correction.bgcolor="green"
        else  :
            text_answer_candidat_in_correction.bgcolor="red"
        print('TXT_ANSWER : ' ,TXT_ANSWER) 
        page.update()



    def go_next_question(e):
        
        n=int(B_number_question.content.value.split("-")[1])      
        if n<40 :
            #go_to_specific_question
            go_to_specific_question(n+1)
        else :
            if n==40 :
                go_to_correction()

        page.update()
        

            

    def go_previeous_question(e):
        print("go_previeous_question")
        n=int(B_number_question.content.value.split("-")[1])
        if n>1 :
            n-=1

        #go_to_specific_question
        go_to_specific_question(n)

    def on_click_B_number_question(e):
        '''
        txt=e.control.text
        print(txt)
        [PopupMenuItem(text=f"سؤال-{i+1}",on_click=changeNumberQuestion) for i in range(40) ]
        '''
        

    def ask_restart_yes_no(e):
        page.open(alert_dialog_restart)

    

    def command_restart_no(e):
        page.close(alert_dialog_restart)
        
    def command_restart_yes(e):
        #write file
        write_file_answer_and_info_if_not_exist()

        #go to question 1
        go_to_specific_question(1)

        #close
        page.close(alert_dialog_restart)
        
        
        
        

    def go_to_specific_question(n):
        if VAR_ACTIVATION:
            #save number question txt file
            write_number_quesion(n)

            #upadet name in button li mktbo fih number questio li black
            B_number_question.content.value=f"سؤال-{n}"
            

            #load answer
            #colrer all with red
            for B in list_Buttons  :
                B.bgcolor="#ff585d"

            #read anwer
            f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
            s=f.readlines()
            f.close()

            #clean answer
            answer=s[int(n)].replace("\n","").split(":")[1]
            answer_as_list=answer.split("-") #40:-
            #print(" answer and number question ",n,answer)

            #write answer to text_answer.content.value=new_answer
            text_answer.content.value=answer

            #colorer B_number_question  bach iwlli itbdl l couleur fach doz mn question l question
            color_=["black","white"]
            color_=["black","#468363"]#,"#434040"]
            i_=int(n)%2
            #B_number_question.color=color_[i_]
            B_number_question.bgcolor=color_[1-i_]

            #colorer buttons 
            for i in range(4):
                if f"{i+1}" in answer_as_list : 
                    B=list_Buttons[i]
                    B.bgcolor="blue"
        else :
            show_alerte_activation()

            

        #update
        page.update()


    def changeWidget(e):
        print('changeWidget')
        
        index=int(e.control.selected_index)
        #hide_all()
        hide_all()
        
        if index==1 :
            
                if I_AM_WAS_IN_CORRACTION :
                    go_to_correction()
                else :
                    print("visible")
                    #page.add(column_answer,row_next_back)
                    column_answer.visible=True
                    row_next_back.visible=True
                    B_restart.visible=True
            

            
        else :
            #show
            row_copy_save.visible=True
            text_writre_trueAnswer.visible=True
        page.update()
        
        print("index",index)

    def command_ask_yesy_no_to_save(e):
        print('command_ask_yesy_no_to_save')
        page.open(alert_dialog_save)

    def command_save_no(e):
        print('command_save_no')
        page.close(alert_dialog_save)

    def command_save_yes(e):
        print('command_save_yes')
        page.close(alert_dialog_save)

        txt=text_writre_trueAnswer.value
        print("text copied" , txt)

        #write answer
        file_answer=DIR_FILE_TRUE_ANSWER
        f=open(file_answer,"w")
        f.write(txt)
        f.close()

        #updtae serie in app bar in ... (hna fach kandakhlo les repons from Qr Code khas la
        #liste dial les series dar liha update
        page.appbar.actions=[
                           PopupMenuButton(
                               items=[
                                PopupMenuItem(text=f"السلسلة-{i+1}",on_click=changeNumberSeire)
                                for i in range(get_number_total_of_series())])
                           ]

        #go to serie number 1
        go_to_serie("السلسلة-1")

        #update page
        page.update()

    def paste_text(e):
        txt=page.get_clipboard()
        text_writre_trueAnswer.value=txt
        page.update()

    def on_click_detele_text(e):
        txt=''
        text_writre_trueAnswer.value=txt
        page.update()
        

    
            

    def write_file_answer_and_info_if_not_exist():
        list_infos=["info:number_serie=1#number_question=1\n"]
        list_answer=[ f"{i}:-\n"  for i  in range(1,41)]
        list_=list_infos+list_answer
        f=open(DIR_FILE_ANSEWER_AND_INFOS,"w")
        f.writelines(list_)
        f.close()
        


    def analyser_file_answer_and_info():
        write_file_answer_and_info_if_not_exist()
        


    


    def go_to_correction():
        #hide_all
                global  TXT_ANSWER,TXT_TRUE_ANSWER,I_AM_WAS_IN_CORRACTION

                I_AM_WAS_IN_CORRACTION=1
    
                #hna khask tkhwi hado bach matb9ach ghir katzid fihom
                TXT_ANSWER=""
                TXT_TRUE_ANSWER=""
                
                hide_all()
                #show
                for row_corr in list_rows_corrections :
                    row_corr.visible=True

                #show
                row_result_back.visible=True

                #divider
                divider_0.visible=True
                divider.visible=True

                

                #show  row_answer_and_true_answer
                row_answer_and_true_answer.visible=True

                #color buttons  rja3
                #get all answer  as text like : 1AB11AB11AB11AB11AB11AB11AB11AB11AB11AB1
                #read answer
                f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
                s=f.readlines()
                f.close()

                #get number serie
                number_serie_=page.appbar.title.value.split('-')[0]
                if "س" in number_serie_ :
                    number_serie_=page.appbar.title.value.split('-')[1]
                    
                
                for i in range(1,41):
                    answer_=s[i].replace("\n","").split(":")[1]
                    
                    TXT_ANSWER+=DIC_ANSWER[answer_]
                #print(TXT_ANSWER)  

                #extact true answer
                f=open(DIR_FILE_TRUE_ANSWER,"r")
                s_corrections=f.readlines()
                f.close()

                for line_txt_true_answer in s_corrections :
                    if "#" in line_txt_true_answer :
                        number_serie_in_line_true_answer=int(line_txt_true_answer.split("#")[0])
                        if  int(number_serie_)==int(number_serie_in_line_true_answer):
                            TXT_TRUE_ANSWER=line_txt_true_answer.split("#")[1]
                #print(TXT_TRUE_ANSWER)

                #colorer  buttons
                count_result=0
                for i in range(40):
                    _answer=TXT_ANSWER[i:i+1]
                    _answer_true=TXT_TRUE_ANSWER[i:i+1]
                    #print("_answer  and _answer_true : " ,_answer, _answer_true)
                    if  _answer==_answer_true :
                        list_all_buttons_corrections[i].bgcolor='green'
                        count_result+=1
                    else :
                        list_all_buttons_corrections[i].bgcolor='red'

                #write result  yyyy
                text_result.text="النتيجة : "+f"{count_result}/40"
                if  count_result<32 :
                    text_result.bgcolor="red"
                if  count_result>31 :
                    text_result.bgcolor="green"

                #page
                page.update()
                    
                
                
                    


    def command_b_back_to_answer(e):
        global  I_AM_WAS_IN_CORRACTION
        #hide_all
        hide_all()

        #I_AM_WAS_IN_CORRACTION
        I_AM_WAS_IN_CORRACTION=0
        

        #show   column_answer  and   row_next_back
        column_answer.visible=True
        row_next_back.visible=True
        B_restart.visible=True
        

        #page.update()
        page.update()



        

    def hide_all():
        #hide
        row_copy_save.visible=False
        text_writre_trueAnswer.visible=False
            
        #hide   column_answer  and   row_next_back
        column_answer.visible=False
        row_next_back.visible=False
            
        #hide  all row in list_rows_corrections
        for row_corr in list_rows_corrections :
                    row_corr.visible=False
        #hide row_result_back
        row_result_back.visible=False

        #row_answer_and_true_answer
        row_answer_and_true_answer.visible=False

        #divider
        divider_0.visible=False
        divider.visible=False

        #B_restart
        B_restart.visible=False

        page.update()



    def write_number_quesion(n):
        f=open(DIR_FILE_NUMBER_QUESTION,"w")
        f.write(str(n))
        f.close()


    def write_number_serie(n):
        f=open(DIR_FILE_NUMBER_SERIE,"w")
        f.write(str(n))
        f.close()

        
        
    def go_serie_and_question_for_demarage():
        #read txt file  #  
        number_serie_=1
        number_question_=1

        try :
            #read number serie   DIR_FILE_NUMBER_QUESTION  DIR_FILE_NUMBER_QUESTION
            f=open(DIR_FILE_NUMBER_SERIE,"r")
            s=f.readlines()
            f.close()
            number_serie_=int(s[0].split("\n")[0].replace(" ",""))
            

            #read number question
            f=open(DIR_FILE_NUMBER_QUESTION,"r")
            ss=f.readlines()
            f.close()
            number_question_=int(ss[0].split("\n")[0].replace(" ",""))

        except :
            pass

        #go to question
        go_to_specific_question(number_question_)

        #write number serie in appbar
        new_serie=f"السلسلة-{number_serie_}"
        page.appbar.title=Text(new_serie)


        
        

    #demarage
    def demarage():
        #go_serie_and_question_for_demarage
        go_serie_and_question_for_demarage()
        #load answer
        #read answer
        file_answer=DIR_FILE_TRUE_ANSWER
        try :
            f=open(file_answer,"r")
            s=f.read()
            f.close()
            #write answer on text_writre_trueAnswer
            text_writre_trueAnswer.value=s
        except :
            f=open(file_answer,"w")
            f.close()
        #page.update()
        page.update()

        #create file DIR_FILE_ANSEWER_AND_INFOS if not exist
        try :
            f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
            s=f.readlines()
            f.close()
            if  "info:number_serie" not in s[0] :
                analyser_file_answer_and_info()
                
        except :
            analyser_file_answer_and_info()


    def show_alerte_activation():
        #test,txt_content=check_stability_serial_number()
        #txt_content="test"
        global VAR_CKECK_SATBILITY,TEXT_CONTENT

        if VAR_ACTIVATION==0:
            #ila makanch serial stable hide all ro and write in  alert_dialog_activation
            #اغلق التطبيق.....
            if VAR_CKECK_SATBILITY==0:
                for row_ in material_actions_activation:
                    if row_!=row_button_close_app:
                        row_.visible=False
                    else  :
                        row_button_close_app.visible=True
                alert_dialog_activation.content.value=TEXT_CONTENT
            else :
                #ila kano mntab9in show all row and write no thing in  alert_dialog_activation
                for row_ in material_actions_activation:
                    if row_!=row_button_close_app:
                        row_.visible=True
                    else :
                        row_button_close_app.visible=False
                        
                alert_dialog_activation.content.value=''
                
            page.open(alert_dialog_activation)
            page.update()

    
        
                
            


    #write_key_activation
    def write_key_activation(e):
        global VAR_ACTIVATION
        txt_activation_=TextField_activation.value
        supposed_key_activation=txt_activation_

        #hna ila dakhl l code dial 2025 parce que hada l code '1234'  ki activer l'application
        #ila knti f 2025
        if   txt_activation_=="1234" :
            #hna khasni nmchi n checki l'anné
            test,error=current_year_is_2025()
            print(test,error)

            #ila kan variment had l3am howa 2025 ghadi n activer lih l'appliction
            #ya3ni   txt_activation_ hadi ghadi iwli
            #txt_activation_=true_activation 
            if test==1 :
                date_creation_as_serial=ACT.get_date_cretaion_assets_as_serial_number()
                true_activation=ACT.create_activation(date_creation_as_serial)
                supposed_key_activation=true_activation
                print(supposed_key_activation)
        
            else :
                TextField_activation.value=error
                
        
        #write key wakaha maykonch shih w mn b3a kan3ay 3la
        #check_activation bach ncho wach dakchi how ahadak olal la
        #XXXXXXXXXXX
        f=open(DIR_FILE_ACTIVATION,'w')
        f.write(str(supposed_key_activation))
        f.close()

        
        #call ACT.check_activation and update  VAR_ACTIVATION 
        VAR_ACTIVATION=ACT.check_activation()
            
        if VAR_ACTIVATION :
            #alert_dialog_activation.visible=False
            page.close(alert_dialog_activation)
        else :
                TextField_activation.value="The code is incorrect, or you are not connected to the internet."

        page.update()
    

    def paste_activation(e):
        txt=page.get_clipboard()        
        TextField_activation.value=txt
        page.update()

    def clear_in_activation(e):
        TextField_activation.value=''
        page.update()

    def copy_mo3arif(e):
        txt_=str(Text_mo3arif.value)
        print(txt_)
        if ":"  in txt_ :
            list_txt_=txt_.split(':')
            mo3arif_=list_txt_[0]
            if "D"  in mo3arif_ :
                mo3arif_=list_txt_[1]
        page.set_clipboard(mo3arif_)
        
        
        
        
            
            
            
        
            
        
    
            
            
            

    
        
        

    
        
        

    
    
    page.title="Code Maroc Android"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    #page.vertical_alignment = MainAxisAlignment.CENTER
    #page.horizontal_alignment = MainAxisAlignment.CENTER
    #page.padding=200
    
    



    #app appbar_seire
    page.appbar=AppBar(bgcolor="red",
                       
                       
                       title=Text("1- السلسة"),
                       center_title=True,
                       

                       actions=[
                           PopupMenuButton(
                               items=[
                                PopupMenuItem(text=f"السلسلة-{i+1}",on_click=changeNumberSeire)
                                for i in range(get_number_total_of_series())])
                           ]
                      
                       
                       
                       

                       )


    #navigation_bar
    page.navigation_bar=NavigationBar(height=60,
        on_change=changeWidget,
        selected_index=0,
        destinations=[
            NavigationBarDestination(icon=Icons.EDIT_DOCUMENT),
            NavigationBarDestination(icon=Icons.HOME)
            ]
        )


    
    
    B_with=300
    B_hieght=60

    """material_actions_activation =[
        TextField(Text(text=str(ACT.get_date_cretaion_assets_as_serial_number())),
        TextButton(text="لا" , on_click=command_restart_no)
    ]
    """
    Text_mo3arif=Text(str(TEXT_CONTENT))
    Button_clear_copy_mo3arif=TextButton(icon=Icons.COPY,on_click=copy_mo3arif)
    row_activation_mo3arif=Row(spacing=20,controls=[Button_clear_copy_mo3arif,Text_mo3arif],alignment="center")

    
    TextField_activation=TextField(width=230)
    row_activation_TextField_activation=Row(spacing=20,controls=[TextField_activation],alignment="center")


    Button_activation=TextButton(text="Activate",on_click=write_key_activation)
    Button_paste_activation=TextButton(icon=Icons.CONTENT_PASTE,on_click=paste_activation)
    Button_clear_activation=TextButton(icon=Icons.DELETE,on_click=clear_in_activation)

    button_close_app=TextButton(text="Close App-إغلاق",icon=Icons.CLOSE,on_click=lambda e:page.window.destroy())

    txt_info_2025_arabic="إذا كنت في سنة 2025 : اتصل بالانترنيت ثم ادخل الكود 1234 و اضغط على زر تفعيل."
    txt_info_2025_english="*If you are in the year 2025,connect to\nthe internet, then enter the code\n '1234' and press the Activate button."
    txt_info_2025=txt_info_2025_arabic+"\n"+txt_info_2025_english
    txt_info_2025=txt_info_2025_english
    text_info_activate_if_2025=Text(txt_info_2025)
    
    

    
    row_in_activation_buttons=Row(spacing=20, controls=[Button_clear_activation,
                                                        Button_paste_activation,
                                                        Button_activation],alignment="center")

    

    row_info_activate_if_2025=Row(spacing=20, controls=[text_info_activate_if_2025],alignment="center")
    row_button_close_app=Row(spacing=20, controls=[button_close_app],alignment="center")

    #
    material_actions_activation=[row_activation_mo3arif,
                                 row_activation_TextField_activation,
                                 row_in_activation_buttons,row_info_activate_if_2025,
                                 row_button_close_app]

    #xxxxxx
    
    alert_dialog_activation=AlertDialog(
                    title=Text("Activation"),
                    content=Text(''),
                    actions=material_actions_activation
                    )

    

    #B_restart
    B_restart = FilledButton(content=Text("إبدأ من جديد",size=15),bgcolor="black",color="white",width=B_with, height=50
                                     ,on_click=ask_restart_yes_no)

    #material_actions 
    material_actions_restart = [
        TextButton(text="نعم",on_click=command_restart_yes),
        TextButton(text="لا" , on_click=command_restart_no),
    ]
    #alert_dialog_restart
    alert_dialog_restart=AlertDialog(
                    title=Text("البدء من جديد"),content=Text("هل تريد البدء من جديد ؟"),
                    actions=material_actions_restart
                    )

    #
    page.add(B_restart)
    
    
    B_number_question = FilledButton(content=Text("سؤال-1",size=SIZE_TEXT_NUMBER_QUESTION)
                                     ,bgcolor="black",color="white",width=int(B_with/2), height=40
                                     ,on_click=on_click_B_number_question)

    #
    text_answer=TextButton(content=Text("-",size=SIZE_TEXT), width=B_with, height=40)

    B1=FilledButton(content=Text("1",size=SIZE_TEXT),bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    B2=FilledButton(content=Text("2",size=SIZE_TEXT),bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    B3=FilledButton(content=Text("3",size=SIZE_TEXT),bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    B4=FilledButton(content=Text("4",size=SIZE_TEXT),bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    list_Buttons=[B1,B2,B3,B4]
    
    list_number_question_text_answser=[text_answer]

    B_back=FilledButton(content=Text("<",size=25),bgcolor="black",color="white",width=int(B_with/4)-5
                        ,on_click=go_previeous_question,height=H_BUTTON_BACK)
    B_next=FilledButton(content=Text(">",size=25),bgcolor="black",color="white",width=int(B_with/4)-5
                        ,on_click=go_next_question,height=H_BUTTON_BACK)
    #row_next_back
    row_next_back=Row(spacing=10, controls=[B_back,B_number_question,B_next],alignment="center")

    column_answer=Column(spacing=20, controls=list_number_question_text_answser+list_Buttons                         
                        )


    #TextAnswer
    text_writre_trueAnswer=TextField(multiline=True,min_lines=7,max_lines=7,width=400)
    
    #B_paste
    B_paste=FilledButton(text="لصق",icon=Icons.CONTENT_PASTE,on_click=paste_text)

    #
    #B_paste
    B_delete=FilledButton(text="مسح",icon=Icons.DELETE,on_click=on_click_detele_text)

    
        

    #material_actions 
    material_actions = [
        TextButton(text="نعم",on_click=command_save_yes),
        TextButton(text="لا" , on_click=command_save_no),
    ]
    
    alert_dialog_save=AlertDialog(
                    title=Text("حفظ"),content=Text("هل تريد الحفظ ؟"),
                    actions=material_actions
                    )

    
        
    #B_save
    B_save=FilledButton(text="حفظ",on_click=command_ask_yesy_no_to_save)

    row_copy_save=Row(spacing=20, controls=[B_delete,B_paste,B_save],alignment="center")

    
    

    
    #hide
    row_copy_save.visible=False
    text_writre_trueAnswer.visible=False


    #row_answer_and_true_answer
      
    

    text_answer_candidat_in_correction=FilledButton(text="- : الاجوبة",bgcolor='red', width=63*2)

    text_true_answer_in_correction=FilledButton(text="- : التصحيح",bgcolor='green', width=63*2)

    row_answer_and_true_answer=Row(spacing=10, controls=[text_true_answer_in_correction
                                                         ,text_answer_candidat_in_correction],alignment="center")
    row_answer_and_true_answer.visible=False

    page.add(row_answer_and_true_answer)
    #divider_0
    divider_0=Divider(height=1, color="black")
    divider_0.visible=False
    page.add(divider_0)


    

    #buttons corrections
    
    list_all_buttons_corrections=[]
    for i in range(40):
            b_correction=FilledButton(content=Text(str(i+1),size=20),width=55
                                      ,height=43,bgcolor="blue",on_click=on_click_on_button_correction)
            list_all_buttons_corrections.append(b_correction)

    #list_rows_corrections
    list_rows_corrections=[]
    for j in range(8):
        row_correction=Row(spacing=10, controls=list_all_buttons_corrections[5*j:5*j+5],alignment="center")
        list_rows_corrections.append(row_correction)
        row_correction.visible=False
        page.add(row_correction)

    #divider
    divider=Divider(height=1, color="black")
    divider.visible=False
    page.add(divider)
        
    #row_result_back
    b_back_to_answer=FilledButton(content=Text("<",size=25),bgcolor="black",color="white", width=63*2
                        ,on_click=command_b_back_to_answer,height=H_BUTTON_BACK)

    text_result=FilledButton(text="النتيجة : 40/40",bgcolor='green', width=63*2,height=H_BUTTON_BACK)
    row_result_back=Row(spacing=10, controls=[b_back_to_answer,text_result],alignment="center")
    row_result_back.visible=False

    
    
    
    

    #add
    page.add(column_answer,row_next_back,text_writre_trueAnswer,row_copy_save,row_result_back)
    
    



    #call demarage()
    demarage()

    #show_alerte_activation
    show_alerte_activation()

    #event close
    #page.window.prevent_close = True
    #page.window.on_event = close_app
    
    #page.fullscreen=True
    page.update()


app(main)
