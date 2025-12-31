suffering(charlie, fever).
suffering(charlie, running_nose).
suffering(charlie, headache).
suffering(micky,cough).
suffering(micky, headache).
suffering(micky, running_nose).
suffering(micky, sneezing).
suffering(branda, fever).

have(patient, flu):-suffering(patient, headache),suffering (patient, bodyache),suffering( patient,fever),suffering(patient, running_nose), suffering(patient,cough),suffering(patient,conjuctivitis).
have(patient,measles):-suffering(patient,rash), suffering(patient, fever),suffering(patient,running_nose),suffering (patient,cough),suffering (patient, conjuctivitis).
have(patient, whooping_cough):-suffering(patient, running_nose), suffering (patient,cough),suffering( patient, sneezing).