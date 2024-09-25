import streamlit as st

def next_page():
    st.session_state.page += 1

def prev_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 0
    if 'symptom_history' not in st.session_state:
        st.session_state.symptom_history = []
    if 'name' not in st.session_state:
        st.session_state.name = ''
    if 'email' not in st.session_state:
        st.session_state.email = ''
    if 'age' not in st.session_state:
        st.session_state.age = ''
    if 'mobile_no' not in st.session_state:
        st.session_state.mobile_no = ''

    if st.session_state.page == 0:
        st.title("HEALTHCARE ASSISTANT")
        st.header("User Information")

        st.session_state.name = st.text_input("Name")
        st.session_state.email = st.text_input("Email")
        st.session_state.age = st.text_input("Age")
        st.session_state.mobile_no = st.text_input("Mobile Number")

        
        if st.session_state.age.isdigit():
            age = int(st.session_state.age)
            if age > 40:
                st.subheader("Wellness Tip")
                st.write("Regular cardiovascular exercise helps reduce the risk of heart disease.")
            elif age < 40:
                st.subheader("Wellness Tip")
                st.write("Maintain a balanced diet rich in vitamins and proteins to sustain energy levels.")

        if st.button('Let\'s go...'):
            next_page()

    elif st.session_state.page == 1:
        st.title("Select Your Symptom")
        st.session_state.symptoms = st.selectbox(
            'Select your symptoms',
            options=['Fever', 'Cough', 'Headache', 'Backpain', 'Stomachache', 
                     'Shoulder pain', 'Knee pain', 'Hip pain', 'Neck pain', 
                     'Sinus', 'Eyes twitching', 'Tooth ache', 'Chest pain', 'Ear pain']
        )

       
        severity = st.radio("How severe is your symptom?", ('Mild', 'Moderate', 'Severe'))
        st.session_state.severity = severity

        if st.button('Next'):
            st.session_state.symptom_history.append({'Symptom': st.session_state.symptoms, 'Severity': severity})
            next_page()

        if st.button('Previous'):
            prev_page()

    elif st.session_state.page == 2:
        st.title("Symptom Analysis")
        selected_symptom = st.session_state.symptoms
        
        symptom_details = {
            "Fever": {
                
                "reasons": [
                    "Viral Infections: Common colds and flu can cause fever.",
                    "Bacterial Infections: Such as strep throat or urinary tract infections.",
                    "Heat Exhaustion: Prolonged exposure to high temperatures."
                ],
                "remedies": [
                    "Medication: Take paracetamol or ibuprofen to reduce fever.",
                    "Hydration: Drink plenty of fluids to prevent dehydration.",
                    "Rest: Ensure you get sufficient rest for recovery."
                ],
                "description": "An increase in body temperature, often indicating infection or illness.",
                "doctor_advice": "If the fever lasts more than three days, or if you experience severe symptoms.",
                "health_tips": "Keep your room cool and wear light clothing to help regulate body temperature."
            },
            "Cough": {
                
                "reasons": [
                    "Infections: Such as the common cold or flu.",
                    "Allergies: Reaction to dust or pollen.",
                    "Irritants: Smoke, strong odors, or pollution."
                ],
                "remedies": [
                    "Stay Hydrated: Drink warm fluids to soothe your throat.",
                    "Honey: Can help reduce cough.",
                    "Steam Inhalation: Helps clear nasal passages."
                ],
                "description": "A sudden, forceful expulsion of air from the lungs.",
                "doctor_advice": "If the cough lasts more than a week, or is accompanied by fever.",
                "health_tips": "Avoid smoking and stay away from irritants."
            },
            "Headache": {
                
                "reasons": [
                    "Dehydration: Lack of fluids can lead to headaches.",
                    "Tension: Stress or muscle strain.",
                    "Sinus Issues: Inflammation of sinus cavities."
                ],
                "remedies": [
                    "Hydrate: Drink water to alleviate dehydration.",
                    "Rest: Ensure you get sufficient sleep.",
                    "Over-the-counter Pain Relievers: Such as ibuprofen."
                ],
                "description": "Pain in the head or face, often described as throbbing or constant.",
                "doctor_advice": "If headaches are frequent or severe, consult a doctor.",
                "health_tips": "Manage stress through relaxation techniques."
            },
            "Backpain": {
                
                "reasons": [
                    "Poor Posture: Sitting for long periods.",
                    "Muscle Strain: Lifting heavy objects improperly.",
                    "Herniated Discs: Discs that compress spinal nerves."
                ],
                "remedies": [
                    "Rest: Avoid strenuous activity.",
                    "Heat/Ice Therapy: Can reduce pain.",
                    "Physical Therapy: Strengthening exercises."
                ],
                "description": "Pain felt in the back, often affecting movement.",
                "doctor_advice": "If pain persists for more than a few days.",
                "health_tips": "Practice good posture and stretch regularly."
            },
            "Stomachache": {
                
                "reasons": [
                    "Indigestion: Eating too quickly or too much.",
                    "Gas: Can cause bloating and pain.",
                    "Gastroenteritis: Infection of the stomach lining."
                ],
                "remedies": [
                    "Ginger Tea: Helps soothe the stomach.",
                    "Hydration: Drink clear fluids.",
                    "Rest: Avoid heavy meals."
                ],
                "description": "Pain in the abdominal area.",
                "doctor_advice": "If pain is severe or lasts more than a day.",
                "health_tips": "Eat small, frequent meals."
            },
            "Shoulder pain": {
                
                "reasons": [
                    "Injury: From sports or falls.",
                    "Repetitive Motion: Such as typing or manual labor.",
                    "Tendonitis: Inflammation of shoulder tendons."
                ],
                "remedies": [
                    "Rest: Avoid activities that worsen pain.",
                    "Ice: Apply ice packs to reduce swelling.",
                    "Physical Therapy: Can help improve range of motion."
                ],
                "description": "Pain in or around the shoulder joint.",
                "doctor_advice": "If pain limits your ability to move your arm.",
                "health_tips": "Engage in regular shoulder strengthening exercises."
            },
            "Knee pain": {
                
                "reasons": [
                    "Injury: From sports or falls.",
                    "Arthritis: Inflammation of the joints.",
                    "Overuse: From repetitive activities."
                ],
                "remedies": [
                    "Rest: Avoid putting weight on the knee.",
                    "Ice: Apply ice packs to reduce swelling.",
                    "Compression: Use a bandage to support the knee."
                ],
                "description": "Pain in or around the knee joint.",
                "doctor_advice": "If pain is severe or persists.",
                "health_tips": "Maintain a healthy weight to reduce stress on knees."
            },
            "Hip pain": {
                
                "reasons": [
                    "Arthritis: Common in older adults.",
                    "Injury: From falls or sports.",
                    "Tendonitis: Inflammation of hip tendons."
                ],
                "remedies": [
                    "Rest: Avoid activities that worsen pain.",
                    "Physical Therapy: Strengthening and flexibility exercises.",
                    "Over-the-counter Pain Relievers: For temporary relief."
                ],
                "description": "Pain in or around the hip joint.",
                "doctor_advice": "If pain affects your mobility.",
                "health_tips": "Stay active with low-impact exercises."
            },
            "Neck pain": {
                
                "reasons": [
                    "Poor Posture: Prolonged sitting or looking down.",
                    "Injury: Whiplash from accidents.",
                    "Muscle Strain: From sleeping awkwardly."
                ],
                "remedies": [
                    "Ice/Heat Therapy: To relieve pain.",
                    "Gentle Stretches: To improve flexibility.",
                    "Over-the-counter Pain Relievers: For short-term relief."
                ],
                "description": "Pain in the neck area, often related to tension.",
                "doctor_advice": "If pain persists or worsens.",
                "health_tips": "Maintain good posture and take breaks."
            },
            "Sinus": {
                
                "reasons": [
                    "Allergies: Reaction to pollen or dust.",
                    "Infections: Such as sinusitis.",
                    "Nasal Blockage: Caused by colds or flu."
                ],
                "remedies": [
                    "Steam Inhalation: Helps clear sinuses.",
                    "Saline Nasal Spray: To relieve congestion.",
                    "Stay Hydrated: Drink plenty of fluids."
                ],
                "description": "Pressure or pain in the sinus cavities.",
                "doctor_advice": "If symptoms persist beyond a week.",
                "health_tips": "Avoid allergens when possible."
            },
            "Eyes twitching": {
                
                "reasons": [
                    "Fatigue: Lack of sleep can cause twitching.",
                    "Stress: Can lead to involuntary muscle movements.",
                    "Caffeine: Excessive intake may trigger twitching."
                ],
                "remedies": [
                    "Rest: Ensure you get enough sleep.",
                    "Reduce Caffeine: Cut back on coffee and sodas.",
                    "Stress Management: Practice relaxation techniques."
                ],
                "description": "Involuntary twitching of the eyelid.",
                "doctor_advice": "If twitching persists for an extended period.",
                "health_tips": "Manage stress and stay well-rested."
            },
            "Toothache": {
                
                "reasons": [
                    "Cavity: Decay in a tooth.",
                    "Gum Disease: Inflammation of gums.",
                    "Injury: From trauma to the mouth."
                ],
                "remedies": [
                    "Salt Water Rinse: Helps reduce inflammation.",
                    "Pain Relievers: Over-the-counter medications.",
                    "Visit a Dentist: For a thorough examination."
                ],
                "description": "Pain in or around a tooth.",
                "doctor_advice": "If pain is severe or persistent.",
                "health_tips": "Maintain good oral hygiene."
            },
            "Chest pain": {
                
                "reasons": [
                    "Heart Issues: Can indicate serious conditions.",
                    "Muscle Strain: From lifting or physical activity.",
                    "Gastrointestinal Issues: Such as acid reflux."
                ],
                "remedies": [
                    "Rest: Stop any activity that causes pain.",
                    "Deep Breathing: Can help reduce anxiety.",
                    "Seek Immediate Medical Attention: If pain is severe."
                ],
                "description": "Discomfort or pain in the chest area.",
                "doctor_advice": "If pain is severe or accompanied by other symptoms.",
                "health_tips": "Know the signs of heart problems."
            },
            "Ear pain": {
                
                "reasons": [
                    "Ear Infection: Common in children.",
                    "Fluid Buildup: From allergies or colds.",
                    "Earwax Buildup: Can cause discomfort."
                ],
                "remedies": [
                    "Warm Compress: Helps reduce pain.",
                    "Pain Relievers: Over-the-counter options.",
                    "Consult a Doctor: If pain persists."
                ],
                "description": "Pain in or around the ear.",
                "doctor_advice": "If pain lasts more than a few days.",
                "health_tips": "Keep ears dry and clean."
            }
        }

        if selected_symptom in symptom_details:
            details = symptom_details[selected_symptom]
            st.subheader("Description")
            st.write(details["description"])
            st.subheader("Reasons")
            st.write("\n".join(details["reasons"]))
            st.subheader("Remedies")
            st.write("\n".join(details["remedies"]))
            st.subheader("Doctor's Advice")
            st.write(details["doctor_advice"])
            st.subheader("Health Tips")
            st.write(details["health_tips"])

            # Medication Reminder Feature
            if st.session_state.severity == 'Severe':
                if st.checkbox('Set medication reminder'):
                    st.write("Reminder set for taking medication every 6 hours.")

            if st.button('Previous'):
                prev_page()

            if st.button('View Dashboard'):
                next_page()

    elif st.session_state.page == 3:
        st.title("Health Dashboard")

        # Track Symptoms Over Time
        if len(st.session_state.symptom_history) > 0:
            st.write("Your Symptom History:")
            for i, record in enumerate(st.session_state.symptom_history, 1):
                st.write(f"{i}. {record['Symptom']} - {record['Severity']}")
        else:
            st.write("No symptoms tracked yet.")

        # User Information for Report
        user_info = f"Name: {st.session_state.name}\nEmail: {st.session_state.email}\nAge: {st.session_state.age}\nMobile Number: {st.session_state.mobile_no}\n"

        # Get Remedies and Additional Info for Report
        symptom_info = {
            "Fever": {
                "remedies": [
                    "Medication: Take paracetamol or ibuprofen to reduce fever.",
                    "Hydration: Drink plenty of fluids to prevent dehydration.",
                    "Rest: Ensure you get sufficient rest for recovery."
                ],
                "description": "An increase in body temperature, often indicating infection or illness.",
                "doctor_advice": "If the fever lasts more than three days, or if you experience severe symptoms.",
                "health_tips": "Keep your room cool and wear light clothing to help regulate body temperature."
            },
            "Cough": {
        "remedies": [
            "Stay Hydrated: Drink warm fluids to soothe your throat.",
            "Honey: Can help reduce cough.",
            "Steam Inhalation: Helps clear nasal passages."
        ],
        "description": "A sudden, forceful expulsion of air from the lungs.",
        "doctor_advice": "If the cough lasts more than a week, or is accompanied by fever.",
        "health_tips": "Avoid smoking and stay away from irritants."
    },
    "Headache": {
        "remedies": [
            "Hydrate: Drink water to alleviate dehydration.",
            "Rest: Ensure you get sufficient sleep.",
            "Over-the-counter Pain Relievers: Such as ibuprofen."
        ],
        "description": "Pain in the head or face, often described as throbbing or constant.",
        "doctor_advice": "If headaches are frequent or severe, consult a doctor.",
        "health_tips": "Manage stress through relaxation techniques."
    },
    "Backpain": {
        "remedies": [
            "Rest: Avoid strenuous activity.",
            "Heat/Ice Therapy: Can reduce pain.",
            "Physical Therapy: Strengthening exercises."
        ],
        "description": "Pain felt in the back, often affecting movement.",
        "doctor_advice": "If pain persists for more than a few days.",
        "health_tips": "Practice good posture and stretch regularly."
    },
    "Stomachache": {
        "remedies": [
            "Ginger Tea: Helps soothe the stomach.",
            "Hydration: Drink clear fluids.",
            "Rest: Avoid heavy meals."
        ],
        "description": "Pain in the abdominal area.",
        "doctor_advice": "If pain is severe or lasts more than a day.",
        "health_tips": "Eat small, frequent meals."
    },
    "Shoulder pain": {
        "remedies": [
            "Rest: Avoid activities that worsen pain.",
            "Ice: Apply ice packs to reduce swelling.",
            "Physical Therapy: Can help improve range of motion."
        ],
        "description": "Pain in or around the shoulder joint.",
        "doctor_advice": "If pain limits your ability to move your arm.",
        "health_tips": "Engage in regular shoulder strengthening exercises."
    },
    "Knee pain": {
        "remedies": [
            "Rest: Avoid putting weight on the knee.",
            "Ice: Apply ice packs to reduce swelling.",
            "Compression: Use a bandage to support the knee."
        ],
        "description": "Pain in or around the knee joint.",
        "doctor_advice": "If pain is severe or persists.",
        "health_tips": "Maintain a healthy weight to reduce stress on knees."
    },
    "Hip pain": {
        "remedies": [
            "Rest: Avoid activities that worsen pain.",
            "Physical Therapy: Strengthening and flexibility exercises.",
            "Over-the-counter Pain Relievers: For temporary relief."
        ],
        "description": "Pain in or around the hip joint.",
        "doctor_advice": "If pain affects your mobility.",
        "health_tips": "Stay active with low-impact exercises."
    },
    "Neck pain": {
        "remedies": [
            "Ice/Heat Therapy: To relieve pain.",
            "Gentle Stretches: To improve flexibility.",
            "Over-the-counter Pain Relievers: For short-term relief."
        ],
        "description": "Pain in the neck area, often related to tension.",
        "doctor_advice": "If pain persists or worsens.",
        "health_tips": "Maintain good posture and take breaks."
    },
    "Sinus": {
        "remedies": [
            "Steam Inhalation: Helps clear sinuses.",
            "Saline Nasal Spray: To relieve congestion.",
            "Stay Hydrated: Drink plenty of fluids."
        ],
        "description": "Pressure or pain in the sinus cavities.",
        "doctor_advice": "If symptoms persist beyond a week.",
        "health_tips": "Avoid allergens when possible."
    },
    "Eyes twitching": {
        "remedies": [
            "Rest: Ensure you get enough sleep.",
            "Reduce Caffeine: Cut back on coffee and sodas.",
            "Stress Management: Practice relaxation techniques."
        ],
        "description": "Involuntary twitching of the eyelid.",
        "doctor_advice": "If twitching persists for an extended period.",
        "health_tips": "Manage stress and stay well-rested."
    },
    "Toothache": {
        "remedies": [
            "Salt Water Rinse: Helps reduce inflammation.",
            "Pain Relievers: Over-the-counter medications.",
            "Visit a Dentist: For a thorough examination."
        ],
        "description": "Pain in or around a tooth.",
        "doctor_advice": "If pain is severe or persistent.",
        "health_tips": "Maintain good oral hygiene."
    },
    "Chest pain": {
        "remedies": [
            "Rest: Stop any activity that causes pain.",
            "Deep Breathing: Can help reduce anxiety.",
            "Seek Immediate Medical Attention: If pain is severe."
        ],
        "description": "Discomfort or pain in the chest area.",
        "doctor_advice": "If pain is severe or accompanied by other symptoms.",
        "health_tips": "Know the signs of heart problems."
    },
    "Ear pain": {
        "remedies": [
            "Warm Compress: Helps reduce pain.",
            "Pain Relievers: Over-the-counter options.",
            "Consult a Doctor: If pain persists."
        ],
        "description": "Pain in or around the ear.",
        "doctor_advice": "If pain lasts more than a few days.",
        "health_tips": "Keep ears dry and clean."
    }
        }

        symptom_details = symptom_info.get(st.session_state.symptoms, {})
        remedies = symptom_details.get("remedies", [])
        description = symptom_details.get("description", "N/A")
        doctor_advice = symptom_details.get("doctor_advice", "N/A")
        health_tips = symptom_details.get("health_tips", "N/A")

        # Download Symptom Report
        symptom_report = user_info + '\nSymptom History:\n' + \
                         '\n'.join([f"{record['Symptom']} - Severity: {record['Severity']}" for record in st.session_state.symptom_history]) + \
                         '\n\nRemedies:\n' + '\n'.join(remedies) + \
                         '\n\nDescription:\n' + description + \
                         '\n\nWhen to See a Doctor:\n' + doctor_advice + \
                         '\n\nHealth Tips:\n' + health_tips

        st.download_button(label="Download Symptom Report", data=symptom_report.encode('utf-8'), file_name="symptom_report.txt")

        if st.button('Previous'):
            prev_page()

if __name__ == "__main__":
    main()
