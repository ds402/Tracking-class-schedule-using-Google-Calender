#  It create json file
#  This is sample file which you can edit according to your TimeTable
# 'lecSt' stand for Time at which lecture START in ISO format(Don't forget)
# 'lecEd' stand for Time at which lecture END in ISO format(Don't forget)
#  OUTPUTFILE will be generated in WORKING DIR
import json

data = {
             'Monday': [
                   {
                    'start':  {'lecSt': '09:00:00'},
                    'end':    {'lecEd': '11:00:00'},
                    'summary': 'IE (L)',
                    'description' : 'Introduction to Electronics (EC2L001)',
                    'location' : '101,LBC',
                   },
                   {
                    'start':  {'lecSt': '11:00:00'},
                    'end':    {'lecEd': '13:00:00'},
                    'summary': 'SS (L)',
                    'description' : ' Signal and Systems (EC2L002)',
                    'location' : '101,LBC',
                   },
                   {
                    'start':  {'lecSt': '14:30:00'},
                    'end':    {'lecEd': '16:30:00'},
                    'summary': 'Breadth-1',
                    'description' : 'Breadth-1',
                    'location' : 'Somewhere in LBC',
                   }],
            'Tuesday': [
                   {
                    'start':  {'lecSt': '09:00:00'},
                    'end':    {'lecEd': '12:00:00'},
                    'summary': 'SS Lab',
                    'description' : ' Signal and Systems (EC2P002)',
                    'location' : '112,SES',
                   },
                   {
                    'start':  {'lecSt': '14:30:00'},
                    'end':    {'lecEd': '15:30:00'},
                    'summary': 'PSP (T)',
                    'description' : 'Probabality & Stochastic Process (MA2L003)',
                    'location' : '002,LBC',
                   },
                   {
                    'start':  {'lecSt': '15:30:00'},
                    'end':    {'lecEd': '17:30:00'},
                    'summary': 'IMS',
                    'description' : 'Introduction to Material Science and Engineering (ID2L001)',
                    'location' : '102,LBC',
                   }],
            'Wednesday': [
                   {
                    'start':  {'lecSt': '09:00:00'},
                    'end':    {'lecEd': '10:00:00'},
                    'summary': 'SS (L)',
                    'description' : ' Signal and Systems (EC2L002)',
                    'location' : '101,LBC',
                   },
                   {
                    'start':  {'lecSt': '10:00:00'},
                    'end':    {'lecEd': '11:00:00'},
                    'summary': 'IE (L)',
                    'description' : 'Introduction to Electronics (EC2L001)',
                    'location' : '101,LBC',
                   },
                   {
                    'start':  {'lecSt': '11:30:00'},
                    'end':    {'lecEd': '13:30:00'},
                    'summary': 'PSP (L)',
                    'description' : 'Probabality & Stochastic Process (MA2L003)',
                    'location' : '203,LBC',
                   },
                   {
                    'start':  {'lecSt': '15:30:00'},
                    'end':    {'lecEd': '17:30:00'},
                    'summary': 'IBT',
                    'description' : 'Introduction to Bioscience and Technology (ID2L002)',
                    'location' : '101, LBC',
                   }],
             'Thursday': [
                   {
                    'start':  {'lecSt': '10:00:00'},
                    'end':    {'lecEd': '11:00:00'},
                    'summary': 'PSP (L)',
                    'description' : 'Probabality & Stochastic Process (MA2L003)',
                    'location' : '203,LBC',
                   }, 
                   {
                    'start':  {'lecSt': '11:00:00'},
                    'end':    {'lecEd': '12:00:00'},
                    'summary': 'IE (T)',
                    'description' : 'Introduction to Electronics (EC2L001)',
                    'location' : '201,LBC',
                   },
                   {
                    'start':  {'lecSt': '12:00:00'},
                    'end':    {'lecEd': '13:00:00'},
                    'summary': 'SS (T)',
                    'description' : ' Signal and Systems (EC2L002)',
                    'location' : '201,LBC',
                   },
                   {
                    'start':  {'lecSt': '14:30:00'},
                    'end':    {'lecEd': '17:30:00'},
                    'summary': 'IE Lab',
                    'description' : 'Introduction to Electronics (EC2P001)',
                    'location' : '004, LBC',
                   }],
             'Friday': [
                   {
                    'start':  {'lecSt': '11:00:00'},
                    'end':    {'lecEd': '13:00:00'},
                    'summary': 'Breadth-1',
                    'description' : 'Breadth-1',
                    'location' : 'Somewhere in LBC',
                   }],
       }

outfile='timetable.json'
with open(outfile,'wb') as f:
   json.dump(data,f)
f.close()


      
      








