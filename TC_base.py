import warnings
import time


warnings.simplefilter ("ignore")

#Below Module is used to wirte the logs to a log file
def loginfo (log):
    etime = time.time();
    ltime = time.ctime(etime);
    print ('{} {}'.format(ltime, log), file=open("log.txt", "a"));
    

#Below Module is used to state if a TC is passed or failed
def printTestStatus(status):
    count = 0
    
    for x in status:
        tc_name      = x.get('tc_name')
        tc_purpose  = x.get('tc_purpose')
        tc_status     = x.get('tc_status')
        tc_error       = x.get('tc_error')  if (x.get('tc_error')) else 0
		
        if (tc_error):
            info = "\"[{}]\" \"[{}]\" \"[{}]\"".format (tc_status, tc_name, tc_purpose, );
            loginfo (info); 
            info = "Reason: \"{}\"".format(tc_error)	
            loginfo (info);
            count +=1
        else:
            info = "\"[{}]\" \"[{}]\" \"[{}]\"".format (tc_status, tc_name, tc_purpose, );
            loginfo (info); 
		
    if (count):
        loginfo("There are few tests failed")
	
	
#Below Module is used to validate and compare the expected output to actual output
def validation( dct, http_code, error_message = None):
    if dct.get('expected_http_code') == http_code :
        pass
    else:
        return "The HTTP code is {} but {} was expected ".format(http_code, dct.get('expected_http_code'))
		
    if dct.get('expected_error_message') == error_message :
        pass
    else:
        return "The HTTP code is {} but {} was expected ".format(error_message, dct.get('expected_error_message'))

