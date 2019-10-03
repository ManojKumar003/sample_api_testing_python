from TC_base import  *
import requests
import json
import sys


c1 = "localhost"

tcStatus = []

def post (path, req, addr):
    cmd = "http://{}:8080/api/{}".format (addr, path);
    header = {'accept': 'application/json'}
    loginfo ("== Executing command ==")
    info = "curl -X POST \"{}\" \"{}\"".format (cmd, req);
    loginfo (info);
    resp = requests.post (cmd, json = req);

    resp = resp.json ()
    loginfo ("Command output is :");
    loginfo (resp);

    try:
        return resp["id"]
    except KeyError:
        print ("error:", resp)
        raise
    return resp
	
def simulation (path, addr):
    cmd = "http://{}:8080/{}".format (addr, path);
    header = {'accept': 'application/json'}
    loginfo ("== Executing command ==")
    info = "curl -X POST \"{}\" ".format (cmd);
    loginfo (info);
    resp = requests.post (cmd);

  
    loginfo ("Command output is :");
    loginfo (resp.text);
	
    return resp

def getlist (path, addr):
    cmd = "http://{}:8080/api/{}".format (addr, path);
    header = {'accept': 'application/json'}
    loginfo ("== Executing command ==")
    info = "curl -X GET \"{}\"".format (cmd);
    loginfo (info);
    
    resp = requests.get (cmd, headers = header)
    loginfo ("Command output is :");
    loginfo (resp.text);
	
    return resp

def delete (path, addr, id):
    cmd = "http://{}:8080/api/{}/{}".format (addr, path, id);
    header = {'content-type': 'application/json'}
    loginfo ("== Executing command ==")
    info = "curl -X DELETE \"{}\"".format (cmd);
    loginfo (info);
    resp = requests.delete (cmd , headers = header);
    loginfo ("Command output is :");
    loginfo (resp.text);
	
    try:
        pass
    except KeyError:
        print ("error:", resp)
        raise
    return resp

def find (path, addr):
    l = getlist (path, addr)
    return l

def getFightResp (src):
    loginfo ("\n=============Geting Response For Correct Api=============")
    path = "flights"
    tc_purpose = "Geting Response For Correct Api Format"
    ret = find (path, src)
    if ret.status_code == 200 :
        text = json.loads(ret.text)
        expectedStatus = { "expected_http_code" : 200  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None)
        if (status):
            tcStatus.append({'tc_name':'getFightResp', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'getFightResp', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        info = "Received fight data : {}".format (ret.text);
        loginfo (info)
        tcStatus.append({'tc_name':'getFightResp', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})
    
    return ret.status_code

def getFightRespNeg (src):
    loginfo ("\n=============Geting Response For Wrong Api=============")
    path = "flights-test"
    tc_purpose = "Geting Response For Wrong Api Format"
    ret = find (path, src)
	
    if ret.status_code == 404 :
        expectedStatus = { "expected_http_code" : 404  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None)
        if (status):
            tcStatus.append({'tc_name':'getFightRespNeg', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'getFightRespNeg', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        tcStatus.append({'tc_name':'getFightRespNeg', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})
		
    return ret.status_code

def getFightData (src):
    loginfo ("\n=============Geting Response For Correct Flight-ID=============")
    path = "flights/FL-1567"
    tc_purpose = "Geting Response For Correct Flight-ID"
    ret = find (path, src)

    if ret.status_code == 200 :
        text = json.loads(ret.text)
        expectedStatus = { "expected_http_code" : 200  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None)
        if (status):
            tcStatus.append({'tc_name':'getFightData', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'getFightData', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        info = "Received fight data : {}".format (ret.text);
        loginfo (info)
        tcStatus.append({'tc_name':'getFightData', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})
        
    
    return ret.status_code

def getFightDataNeg (src):
    loginfo ("\n=============Geting Response For Wrong Flight-ID=============")
    path = "flights/2133"
    tc_purpose = "Geting Response For Wrong Flight-ID"
    ret = find (path, src)
    if ret.status_code == 400 :
        text = json.loads(ret.text)
        expectedStatus = { "expected_http_code" : 400 , "expected_error_message" : "Path parameter doesn't represent a valid flight number:" }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = text[0].get('message') )
        if (status):
            tcStatus.append({'tc_name':'getFightDataNeg', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'getFightDataNeg', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        info = "Received fight data : {}".format (ret.text);
        loginfo (info)
        tcStatus.append({'tc_name':'getFightDataNeg', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})
    
    return ret.status_code


def deleteFight (src,):
    loginfo ("\n=============Delete Flight Data=============")
    path = "flights"
    id = "FL-1567"
    tc_purpose = "Deleting Flight data with correct/valid Flight-ID"
    ret = delete (path, src, id)
	
    if ret.status_code == 204 :
        expectedStatus = { "expected_http_code" : 204  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None )
        if (status):
            tcStatus.append({'tc_name':'deleteFight', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'deleteFight', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        tcStatus.append({'tc_name':'deleteFight', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})   

def deleteFightNeg (src,):
    loginfo ("\n=============Delete Flight Data=============")
    path = "flights"
    id = "FL-1234"
    tc_purpose = "Deleting Flight data with correct/valid Flight-ID"
    ret = delete (path, src, id)
	
    if ret.status_code == 404 :
        expectedStatus = { "expected_http_code" : 404  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None )
        if (status):
            tcStatus.append({'tc_name':'deleteFightNeg', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'deleteFightNeg', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        tcStatus.append({'tc_name':'deleteFightNeg', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})   

def getSimulation (src):
    loginfo ("\n=============Geting Response For Correct Flight-ID=============")
    path = "simulation.html"
    tc_purpose = "Simulation Test-Case"
    ret = simulation (path, src)

    if ret.status_code == 200 :
        expectedStatus = { "expected_http_code" : 200  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None)
        if (status):
            tcStatus.append({'tc_name':'getSimulation', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'getSimulation', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        tcStatus.append({'tc_name':'getSimulation', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})
        
    
    return ret.status_code

def postFight (addr):
    loginfo ("\n============Create a Flight data============")
    path = "flights"
    tc_purpose = "Create a Flight data"
    req = { "name" : 'FL-1234',
              }
    ret = post (path, req, addr)
    info = "Replication {}: {}".format (name, ret)
    loginfo (info);
    if ret.status_code == 200 :
        text = json.loads(ret.text)
        expectedStatus = { "expected_http_code" : 200  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None)
        if (status):
            tcStatus.append({'tc_name':'postFight', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'postFight', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        info = "Received fight data : {}".format (ret.text);
        loginfo (info)
        tcStatus.append({'tc_name':'postFight', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})
    return ret

def postFightNeg (addr):
    loginfo ("\n============Create a Flight data============")
    path = "flights"
    tc_purpose = "Create a Flight data"
    req = { "name" : 'FL-1234',
              }
    ret = post (path, req, addr)
    info = "Replication {}: {}".format (name, ret)
    loginfo (info);
    if ret.status_code == 200 :
        text = json.loads(ret.text)
        expectedStatus = { "expected_http_code" : 200  }
        status = validation( expectedStatus, http_code = ret.status_code , error_message = None)
        if (status):
            tcStatus.append({'tc_name':'postFight', 'tc_purpose':tc_purpose, 'tc_status': 'fail', 'tc_error': status})
        else:
            tcStatus.append({'tc_name':'postFight', 'tc_purpose':tc_purpose, 'tc_status': 'pass' })
        			
    else:
        info = "Wrong HTTP Status Code value: {}".format (ret.status_code);
        loginfo (info)
        info = "Received fight data : {}".format (ret.text);
        loginfo (info)
        tcStatus.append({'tc_name':'postFight', 'tc_purpose':tc_purpose,'tc_status': 'fail', 'tc_error': 'Test-Case was expected to pass but failed'})
    return ret

def setup ():
    # Getting Response Codes
    getFightResp (c1)
    getFightRespNeg (c1)
	
    # Getting Flight Details
    getFightData (c1)
    getFightDataNeg (c1)
	
    # Creating Flight Details
    #postFight (c1)
    #postFightNeg (c1)
	
    # Delete Flight Data
    deleteFight(c1)
    deleteFightNeg (c1)
	
	
	# Simulation Flight Data
    getSimulation(c1)
    
    loginfo ("test-Cases Status is :");
    #print (tcStatus)
    printTestStatus( tcStatus )

if __name__ == "__main__":
    # read commandline arguments, first
    fullCmdArguments = sys.argv

    if len(sys.argv) == 1:
        setup ()

    
