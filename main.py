from patient import Patient, VertebralColumnReport
from FuzzyKnn import knn
from headers import *
from mail import sendmail

label = {'DH' : 'Disk Hernia', 'NO' : 'Normal', 'SL' : 'Spondilolysthesis'}

def printdetails(user, predicted, probability):
    print()
    print('DETAILED REPORT FOR PATIENT {}'.format(user.name))
    print('Diagnosed: {}'.format(label[predicted]))
    accuracy = probability[predicted]
    print('Accuracy: {}%'.format(accuracy))
    print()

    if predicted != 'NO' and accuracy > 75:
        action = 'Booked Follow-up Appointment\nReference for Speciality Hospital also forwarded.\n'
        print('-'*60)
        # call Appointment Scheduler Module
        print('Follow Up Appointment Scheduled with priority : HIGH')
        print('-'*60)
        # call reference builder
        print('Forwarded report for reference with Speciality Hospital')
        print('-'*60)

    elif (predicted != 'NO' and accuracy > 50):
        action = 'Booked Follow-up Appointment'
        # call Appointment Scheduler Module
        print('-'*60)
        print('Follow Up Appointment Scheduled with priority : MODERATE')
        print('-'*60)

    else :
        action = 'Booked Follow-up Appointment'
        print('-'*60)
        # call Appointment Scheduler Module
        print('Follow Up Appointment Scheduled with priority : LOW')
        print('-'*60)

    msg = 'Diagnosed: {}\nAccuracy: {}\n{}'.format(label[predicted], accuracy, action)
    # print(msg, user.email)
    sendmail(user.email, msg)

def main():
    user = Patient.from_input()
    report_path = input('Report Path: ')

    with open(report_path) as file:
        report = json.load(file)

    vcr = VertebralColumnReport(user, report)
    data = pd.DataFrame(vcr.todict(), index=[0])

    predicted, predicted_proba = knn(data)

    probability = {'DH' : predicted_proba[0][0]*100, 'NO' : predicted_proba[0][1]*100, 'SL' : predicted_proba[0][2]*100}

    printdetails(user, predicted[0], probability)

if __name__ == '__main__':
    main()
