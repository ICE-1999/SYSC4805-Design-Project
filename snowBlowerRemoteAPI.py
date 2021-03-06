# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
# Testing line

try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')
    
    
    # Initializing the 
    
    # [leftSensorReturnCode, leftHandle] = sim.simxGetObjectHandle(clientID, "VisionSensorLeft", sim.simx_opmode_blocking)
    # [centerSensorReturnCode, centerHandle] = sim.simxGetObjectHandle(clientID, "VisionSensorCenter", sim.simx_opmode_blocking)
    # [rightSensorReturnCode, rightHandle] = sim.simxGetObjectHandle(clientID, "VisionSensorRight", sim.simx_opmode_blocking)
    # sensors are then saved in the following tuple
    # visionSensor = (leftHandle, centerHandle, rightHandle)

    # Initialization of the Motor joints
    [leftMotorReturnCode, leftJoint] = sim.simxGetObjectHandle(clientID, "LeftMotor", sim.simx_opmode_blocking)
    [rightMotorReturnCode, rightJoint] = sim.simxGetObjectHandle(clientID, "RightMotor", sim.simx_opmode_blocking)
    [chuteMotorReturnCode, chuteJoint] = sim.simxGetObjectHandle(clientID, "ChuteMotor", sim.simx_opmode_blocking)
    print(leftMotorReturnCode, rightMotorReturnCode, chuteMotorReturnCode)
    NOMINAL_VELOCITY = 1 # Nominal velocisty that will be used
    VAR = 1

    while True:
        rightV = NOMINAL_VELOCITY
        leftV = NOMINAL_VELOCITY
        chuteV = NOMINAL_VELOCITY

        leftSensorReturnCode = sim.simxSetJointTargetVelocity(clientID, leftJoint, leftV, sim.simx_opmode_blocking)
        rightSensorReturnCode = sim.simxSetJointTargetVelocity(clientID, rightJoint, rightV, sim.simx_opmode_blocking)
        chuteMotorReturnCode = sim.simxSetJointTargetVelocity(clientID, chuteJoint, chuteV, sim.simx_opmode_blocking)

    # while True:
    #     # Let's get this party Started
    #     defaultReading = (False, False, False)
    #     sensorReading = list(defaultReading)

    #     for i in range(0, 3):
    #         returnBool, state, aux = sim.simxReadVisionSensor(clientID, visionSensor[i], sim.simx_opmode_blocking)
    #         if state > -1:
    #             sensorReading[i] = aux[0][11] < 0.3

    #     rightV = NOMINAL_VELOCITY
    #     leftV = NOMINAL_VELOCITY

    #     if sensorReading[0]:
    #         leftV = -0.03
    #     if sensorReading[2]:
    #         rightV = -0.03

    #     leftSensorReturnCode = sim.simxSetJointTargetVelocity(clientID, leftJoint, leftV, sim.simx_opmode_blocking)
    #     rightSensorReturnCode = sim.simxSetJointTargetVelocity(clientID, rightJoint, rightV, sim.simx_opmode_blocking)






    # Moves left motor forward at 1 speed
    leftMotorReturnCode = sim.simxSetJointTargetVelocity(clientID, leftJoint, -1, sim.simx_opmode_blocking)
    time.sleep(10) # sleep for 10 seconds and run
    leftMotorReturnCode = sim.simxSetJointTargetVelocity(clientID, leftJoint, 0, sim.simx_opmode_blocking)
    # Off

    # Rest of the Code should be written here
    sim.simxGetPingTime(clientID)

    sim.simxFinish(clientID)
    # # Now try to retrieve data in a blocking fashion (i.e. a service call):
    # res,objs=sim.simxGetObjects(clientID,sim.sim_handle_all,sim.simx_opmode_blocking)
    # if res==sim.simx_return_ok:
    #     print ('Number of objects in the scene: ',len(objs))
    # else:
    #     print ('Remote API function call returned with error code: ',res)
    #
    # time.sleep(2)
    #
    # # Now retrieve streaming data (i.e. in a non-blocking fashion):
    # startTime=time.time()
    # sim.simxGetIntegerParameter(clientID,sim.sim_intparam_mouse_x,sim.simx_opmode_streaming) # Initialize streaming
    # while time.time()-startTime < 5:
    #     returnCode,data=sim.simxGetIntegerParameter(clientID,sim.sim_intparam_mouse_x,sim.simx_opmode_buffer) # Try to retrieve the streamed data
    #     if returnCode==sim.simx_return_ok: # After initialization of streaming, it will take a few ms before the first value arrives, so check the return code
    #         print ('Mouse position x: ',data) # Mouse position x is actualized when the cursor is over CoppeliaSim's window
    #     time.sleep(0.005)
    #
    # # Now send some data to CoppeliaSim in a non-blocking fashion:
    # sim.simxAddStatusbarMessage(clientID,'Hello CoppeliaSim!',sim.simx_opmode_oneshot)
    #
    # # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    # sim.simxGetPingTime(clientID)
    #
    # # Now close the connection to CoppeliaSim:
    # sim.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
