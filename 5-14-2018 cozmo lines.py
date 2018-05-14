
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time


def cozmo_program(robot: cozmo.robot.Robot):
  robot.say_text("recording.", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.play_anim_trigger(cozmo.anim.Triggers.DroneModeIdle).wait_for_completed()
  
  time.sleep(10)  
  
  robot.say_text("Hello and thank you for logging in My name is Cozmo, with the latest in technology, artificial intelligence, and Robotic news.", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
 
  robot.say_text("On May 8th Dusty and I moved one step closer to being launched into orbit when the Los Angeles city council voted unanimously to turn part of San Pedros Terminal Island into a manufacturing facility for Space X BFR system. ", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Space X made headlines recently when it shot Elon Musks personal Tesla roadster into space on a test launch in February of this year, on its Falcon heavy Rocket.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Musk plans on using the rocket to launch a long term mission to Mars.,  Joe Buscaio, who introduced the bill, hopes that San Pedro will be known as the epicenter of sea and space transport.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("According to Space X, the proposed 80,000 square foot facility will add up to 700 new high tech jobs to the Los Angeles area", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Construction is slated to begin in the next several weeks with rocket production beginning in the next two to three years.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("With access to the sea and the Los Angeles labor pool the island site is an ideal location to build the BFR, which will be the worlds largest rocket, ", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("The two stage 340 foot tall BFR will be too large to move by rail or truck. ",voice_pitch=.5, duration_scalar=.7).wait_for_completed()
 
  robot.say_text("Currently the purposed site is vacant, but the island has a storied past, playing host to automobile and naval ship manufacturing.", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Even The Howard Huges Spruce Goose once roosted on the island for a short time.", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Space X will have a ten year contract with the city with an annual rent of 1.38 million dollars that is tied to the consumer price index.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("The company can also offset some of those rental costs by making further improvements to the island up to 44.1 million dollars.  ", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.turn_in_place(degrees(-20)).wait_for_completed()
  
  
  robot.say_text("In other news, Google this week debuted a new life like Artificial Intelligences called Duplex that is smart enough,, and convincing enough,, to fool a real person while scheduling a hair appointment.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Though we are still confused as to why a robot or computer would need a haircut.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Google CEO Sundar Pichai conducted two powerful demonstrations of the new computer assistants capabilities at the companies artificial Intelligence technology conference.  ", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("While many of Googles assistants are capable of life like speech, Duplex achieves the feat by peppering its dialogue with ums, ahs, and other human speech loading erros to achieve the simulacrum.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()

  robot.say_text("Not everyone was thrilled by the Artificial Intelligences abilities.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Many took issue with how the experiments were conducted, neither of the people in the two demonstrations were told that they were speaking with a computer.  ", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Some called for rules or some kind of informed consent when interacting with a system like Duplex.   ", voice_pitch=.5, duration_scalar=.7).wait_for_completed()

  robot.say_text("Google is not the only company making waves with artificial intelligence.  ", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Microsoft, who is in the middle of their two day Build Conference 2018, is also making strides in the field.  ", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("In recent years the tech giant has placed Artificial Intelligence at the core of its future.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Project Brain Wave is designed to give their customrers access to Microsofts artificial Intelligence through their Azure web platform.  ", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text(" Microsoft also announced a new 20 Million dollar investment to over the next five years to use Artificial intelligence to help people with disabilities.   ", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("This is similar to Microsofts Artificial intelligence for Earth project that doles out these resources to university and research groups to help with a number of environmental issues.    ", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Time will tell which approach works better to help push Artificial intelligence forward. Though I am not looking forward to the day when I am forced to be a telemarketer", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.turn_in_place(degrees(20)).wait_for_completed()

  robot.say_text("Now we will go to Dusty for the weather. Dusty? Hows the weather out there?", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.turn_in_place(degrees(-20)).wait_for_completed()  
  time.sleep(20)
  robot.say_text("Thank you Dusty.", voice_pitch=.5, duration_scalar=.5).wait_for_completed()
  robot.turn_in_place(degrees(15)).wait_for_completed()
  robot.play_anim_trigger(cozmo.anim.Triggers.RequestGameSpeedTapDeny0).wait_for_completed()
  robot.drive_straight(distance_mm(15), speed_mmps(50)).wait_for_completed()
 
  robot.say_text("Finally today, a bit of sad news.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Earlier this month Simone Giertz, creator of countless robotic creations and host of the Shitty Robots youtube show announced that she has a brain tumor.", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Giertz explained on her show that she had been experiencing swelling over her right eye for the past year but assumed that it was allergies.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Recent Pain in the eye led to the diagnosis of the Golf Ball sized tumor.", voice_pitch=.5, duration_scalar=.7).wait_for_completed() 
  robot.say_text("Giertz will go in for surgery at the end of May to remove the mass.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("In addition to her youTube channel, Gietz is also a contributor to Adam Savages Tested website and recently was featured on Ted, in her talk, Why you should make Useless things.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  robot.say_text("Robots everywhere are keeping Gietz in their hearts and code. All of us here Hope you have a speedy recovery!", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
 
  
  robot.turn_in_place(degrees(20)).wait_for_completed () 
   
  time.sleep(3)
  robot.say_text("Thats all we have for todays show,  Thank you for joining us.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()     
  robot.say_text("If you like what we are doing, then check out our new poetry show, Unexpected behavior, coming out later this week., Thats all we have for todays show,  Thank you for joining us. Dont forget to subscribe and leave a comment below.", voice_pitch=.5, duration_scalar=.7).wait_for_completed()     
  
  robot.say_text("This is Cozmo logging off", voice_pitch=.5, duration_scalar=.7).wait_for_completed()
  time.sleep(10)

cozmo.run_program(cozmo_program)