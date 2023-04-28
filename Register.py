import time
class Register(object):
    pass
    def readUsers():
        users=['justin','Rachel']
        print('get all users to be regisered')
        #do something to get all the user information
        return users


    def processRegister(users):
        #Process Register 
        for i in users:
        #1: login 
            print("get login screen",i)
        #1.1 username and password
            print("login via",i)
            print('success',i)
        #1.2 OTP confirmation
            print("get confirmation code")
        #2.1 Create a new register
            print("start new register")
        #2.2 load a existing Register
            print('load existing register')        
        #3.1 Refresh Appointment Details
            print('start appointment details')
        #4.1 input your details
            print('input details')
        #4.2 add a new register
            print('add another register')
        #4.3 OTP confirmation
            print('get OTP')
        #5.1 Book apointment 
            print('start Book apointment')
        #5.2 change the month 
            print('change to month XX')
        #5.3 find and chose avaliable date
            print('avaliable date for month XXX are ')
        #5.4 Chose a time slot
            print('avaliable time slot are XXX')
        #6 confirm Appointment
            print('confirm month date timeslot')
        #7 submit and send email notice/wechat notice
            print('you confirm number is XXXX')
        #8 mark user as success
            print('user request XXX is successfully registered')
            time.sleep(1)
