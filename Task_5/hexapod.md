For this Project#3 

I have mainly used the [article](https://www.rosroboticslearning.com/inverse-kinematics) given in project questionnaire by you guys 

using Geometric Approach given in "EXAMPLE 2" which somewhat resembles with model given in our questionarie
<img width="342" alt="mannipoolathor" src="https://github.com/user-attachments/assets/24bce11c-1ae5-4003-88fa-09dde488e377" />

In this approach, we will derive the trigonometric equations [using sine and cosine rules] by observing the physical structure of the robot/manipulator
as provided by article.

[COXA angle (alpha)]
->for this angle its easy to caluculate it by imagining the top view 

  ![image_2025-04-14_120141494](https://github.com/user-attachments/assets/33ceb0c5-a72c-4267-bceb-75895298a463)
  
->with help of these resources:
  defined ALPHA IN CODE AS {{ alpha = math.degrees(atan2(y, x))  # phi1 (base rotation) }}

[Tibia angle (gamma)]
->Writing about this angle before the Beta angle  because beta ultimately depends on gamma 

 {{ gamma = math.degrees(acos((dist**2 - L2**2 - L3**2) / (2 * L2 * L3)))  # Notice HERE if i take gamma to be -/+ overall configuration of arm will change as elbow down/up }}
 
  youw'll see in my code that i have written something in front of gamma formula let me explain it in detail here
  
  ![image_2025-04-14_123104774](https://github.com/user-attachments/assets/4065253f-bbec-4aef-aafb-ee0599ea5f74)
  
-> well this cos inverse gives two configurations + and - of gamma value since it will be used in beta 
  this will result in completely 2 different configuration of arm we know it as elbow up/down.
  
-> let me assist you understand it by TEST (5) (large negative value one) in my given code 
   in my test 5 i've target coordinates as (5,5,-10)
   using [geogebra](https://www.geogebra.org/calculator) ive made approximate visualisation about how robot arm will look like
   in Local frame.
   
   ->the folllowing result is for gamma set as ( - )
   
   Target Coordinates: (5.0, 5.0, -10.0)
   Joint Angles: [45.0, 17.52, -137.37]°
   Coordinates are reachable
   
   <img width="1226" alt="ELBOW DOWN" src="https://github.com/user-attachments/assets/abd75353-61dd-4723-b377-71f49782fa80" />

   ->the followinhg result is for gamma set as ( + )

   Target Coordinates: (5.0, 5.0, -10.0)
   Joint Angles: [45.0, -174.12, 137.37]°
   Coordinates are reachable
   
   <img width="1231" alt="ELBOW,UP" src="https://github.com/user-attachments/assets/67a499f4-786d-4237-a594-69b90a80c54f" />

As you can see in both images the image with gamma as (-) seems more viable , as arm going near base doesnt make much sense
thats why in my code ive kept gamma as negative to make it more practical 

[Femur angle (Beta)]

 ->Taking refernce from this part in the given article 
 
 ![image_2025-04-14_125221441](https://github.com/user-attachments/assets/fcb8d180-73a6-46a7-9463-8f7215a99850)

  I converted this into python form with small modifications for our model 
  {{ beta = math.degrees(atan2(z_local, x_local) - atan2(L3 * sin(math.radians(gamma)), L2 + L3 * cos(math.radians(gamma)))  }}

  after some testings with extreme values one time it gave "0.00000000000000000034blah" value ig this happened due float
  function so i put a roundoff function.


