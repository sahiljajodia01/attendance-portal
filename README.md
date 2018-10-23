# Attendance Portal
Providing students a way to see their attendance percentage online.

___

This is the home page of the portal.
![screenshot from 2017-09-27 07 26 10](https://user-images.githubusercontent.com/25135893/31454321-b12cf45e-aed2-11e7-96c1-e23007db761c.png)


There is a login button on home page where the teachers can login to their respective accounts. We have used Django Admin for this.
![screenshot from 2017-09-27 07 26 37](https://user-images.githubusercontent.com/25135893/31454423-07e0bc5e-aed3-11e7-9612-e1bea8c3d869.png)


We have imported this content from a **CSV** file containing information about students. We have used **django-import-export** package for this.
![screenshot from 2017-09-27 07 26 56](https://user-images.githubusercontent.com/25135893/31454513-5079a70a-aed3-11e7-81fb-0f8bab3e212c.png)


So the teachers could just change the attendance percentage of all the students one by one and save it to the database.
![screenshot from 2017-09-27 07 27 28](https://user-images.githubusercontent.com/25135893/31454663-c6435f62-aed3-11e7-8a82-268702a2449b.png)

Finally students can navigate to their respective branch -> year -> division -> subject to see their attendance percentage. Note that students need not login to see their percentage.
![screenshot from 2017-09-27 07 27 50](https://user-images.githubusercontent.com/25135893/31454782-46df10d0-aed4-11e7-8041-49472d3225a6.png)

![screenshot from 2017-09-27 07 28 08](https://user-images.githubusercontent.com/25135893/31454810-5afe1f34-aed4-11e7-9961-8bf6fd87b4e7.png)

___

To run this on your PC, clone this repository and after navigating to the repository type the following command in the terminal
```
pip install -r requirements.txt
python manage.py runserver
```
