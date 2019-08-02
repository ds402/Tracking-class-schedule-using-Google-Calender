# GCTT

GOOGLE Calender Time Table

## About

Create your own timetable and add it to your ***GOOGLE Calender*** or generate
your own ***ICS File*** which you can add in any calender application.

## Direction to use this program ?
   
- **Step 1:** Create your timetable by running this command:

  ```sh

  $ python createTT_json.py
  
  
  ```

  TimeTable will saved in `timetable.json`.
  
 - **Step 2:** Here you have to decide whether you want to add 
     timetable in `Google Calender` or generate `ICS` file.
     
 - **Step 3:** If you choose to add event in `Google Calender`:
 
    - **Step (i):** You need to get `client_secret.json` by following the Step 1 from 
    [link](https://developers.google.com/google-apps/calendar/quickstart/python#step_1_turn_on_the_api_name) 
    and saved to your working directory. 
    
    - **Step (ii):** Now run:
    
         ```sh

           $ python add _to_GoogleCal.py
           
         ```
 - **Step 3:** If you choose to generate `ICS` file  will saved as `timetable.ics` in working directory:
 
      - **Step (i):** Run:
      
           ```sh

            $ python generate_ics.py
           
           
           ```

      - **Step (ii):** Import this ICS file to your calender application.       
      
 - **Delete Event:** Run this command:
 
    ```sh

    $ python del_event.py
           
    ```
    
 ## Contributing
 
 Submit pull request or an issue or contact me on [facebook](https://www.facebook.com/aidtya.u.r.dffrnt) for any other information.
 
## License

GPLv3.
      
