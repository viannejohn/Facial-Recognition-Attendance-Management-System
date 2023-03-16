# Facial-Recognition-Attendance-Management-System

What is facial recognition?


A face analyzer is software that identifies or confirms a person's identity using their face. It works by identifying and measuring facial features in an image. Facial recognition can identify human faces in images or videos, determine if the face in two images belongs to the same person, or search for a face among a large collection of existing images. Biometric security systems use facial recognition to uniquely identify individuals during user onboarding or logins as well as strengthen user authentication activity. Mobile and personal devices also commonly use face analyzer technology for device security.


What are the benefits of facial recognition technology?


Some benefits of face recognition systems are as follows:
Efficient security
Facial recognition is a quick and efficient verification system. It is faster and more convenient compared to other biometric technologies like fingerprints or retina scans. There are also fewer touchpoints in facial recognition compared to entering passwords or PINs. It supports multifactor authentication for additional security verification.

Improved accuracy
Facial recognition is a more accurate way to identify individuals than simply using a mobile number, email address, mailing address, or IP address. For example, most exchange services, from stocks to cryptos, now rely on facial recognition to protect customers and their assets.

Easier integration
Face recognition technology is compatible and integrates easily with most security software. For example, smartphones with front-facing cameras have built-in support for facial recognition algorithms or software code.


What are the use cases of facial recognition systems?


The following are some practical applications of a face recognition system:

Fraud detection
Companies use facial recognition to uniquely identify users creating a new account on an online platform. After this is done, facial recognition can be used to verify the identity of the actual person using the account in case of risky or suspicious account activity.

Cyber security
Companies use facial recognition technology instead of passwords to strengthen cybersecurity measures. It is challenging to gain unauthorized access into facial recognition systems, as nothing can be changed about your face. Face recognition software is also a convenient and highly accurate security tool for unlocking smartphones and other personal devices.

Airport and border control
Many airports use biometric data as passports, allowing travellers to skip long lines and walk through an automated terminal to reach their gate faster. Face recognition technology in the form of e-Passports reduces wait times and improves security.

Banking
Individuals authenticate transactions by simply looking at their phone or computer instead of using one-time passwords or two-step verification. Facial recognition is safer as there are no passwords for hackers to compromise. Similarly, some ATM cash withdrawals and checkout registers can use facial recognition for approving payments.

Healthcare
Facial recognition can be used to gain access to patient records. It can streamline the patient registration process in a healthcare facility and autodetect pain and emotion in patients.


How does facial recognition work?


Facial recognition works in three steps: detection, analysis, and recognition.

Detection
Detection is the process of finding a face in an image. Enabled by computer vision, facial recognition can detect and identify individual faces from an image containing one or many people's faces. It can detect facial data in both front and side face profiles.

Computer vision
Machines use computer vision to identify people, places, and things in images with accuracy at or above human levels and with much greater speed and efficiency. Using complex artificial intelligence (AI) technology, computer vision automates extraction, analysis, classification, and understanding of useful information from image data. The image data takes many forms, such as the following:
•	Single images
•	Video sequences
•	Views from multiple cameras
•	Three-dimensional data


Analysis
The facial recognition system then analyzes the image of the face. It maps and reads face geometry and facial expressions. It identifies facial landmarks that are key to distinguishing a face from other objects. The facial recognition technology typically looks for the following:
 
•	Distance between the eyes
•	Distance from the forehead to the chin
•	Distance between the nose and mouth
•	Depth of the eye sockets
•	Shape of the cheekbones
•	Contour of the lips, ears, and chin
 
The system then converts the face recognition data into a string of numbers or points called a face print. Each person has a unique face print, similar to a fingerprint. The information used by facial recognition can also be used in reverse to digitally reconstruct a person's face.
Recognition
Facial recognition can identify a person by comparing the faces in two or more images and assessing the likelihood of a face match. For example, it can verify that the face shown in a selfie taken by a mobile camera matches the face in an image of a government-issued ID like a driver's license or passport, as well as verify that the face shown in the selfie does not match a face in a collection of faces previously captured.
Is facial recognition accurate?
Facial recognition algorithms have near-perfect accuracy in ideal conditions. There is a higher success rate in controlled settings but generally a lower performance rate in the real world. It is difficult to accurately predict the success rate of this technology, as no single measure provides a complete picture.
 
For instance, facial verification algorithms matching people to clear reference images, such as a driver's license or a mugshot, achieve high-accuracy scores. However, this degree of accuracy is only possible with the following:
 
•	Consistent positioning and lighting
•	Clear and unobstructed facial features
•	Controlled colors and background
•	Camera quality and image resolution
 
Another factor that impacts error rates is aging. Over time, changes in the face make it difficult to match photos taken years earlier.
OpenCV uses machine learning algorithms to search for faces within a picture. Because faces are so complicated, there isn’t one simple test that will tell you if it found a face or not. Instead, there are thousands of small patterns and features that must be matched. The algorithms break the task of identifying the face into thousands of smaller, bite-sized tasks, each of which is easy to solve. These tasks are also called classifiers.
For something like a face, you might have 6,000 or more classifiers, all of which must match for a face to be detected (within error limits, of course). But therein lies the problem: for face detection, the algorithm starts at the top left of a picture and moves down across small blocks of data, looking at each block, constantly asking, “Is this a face? … Is this a face? … Is this a face?” Since there are 6,000 or more tests per block, you might have millions of calculations to do, which will grind your computer to a halt.
To get around this, OpenCV uses cascades. What’s a cascade? The best answer can be found in the dictionary: “a waterfall or series of waterfalls.”
Like a series of waterfalls, the OpenCV cascade breaks the problem of detecting faces into multiple stages. For each block, it does a very rough and quick test. If that passes, it does a slightly more detailed test, and so on. The algorithm may have 30 to 50 of these stages or cascades, and it will only detect a face if all stages pass.
The advantage is that the majority of the picture will return a negative during the first few stages, which means the algorithm won’t waste time testing all 6,000 features on it. Instead of taking hours, face detection can now be done in real time.
Cascades in Practice
Though the theory may sound complicated, in practice it is quite easy. The cascades themselves are just a bunch of XML files that contain OpenCV data used to detect objects. You initialize your code with the cascade you want, and then it does the work for you.
Since face detection is such a common case, OpenCV comes with a number of built-in cascades for detecting everything from faces to eyes to hands to legs. There are even cascades for non-human things. 
