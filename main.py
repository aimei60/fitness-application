from database import SessionLocal, Base, workouts, workout_sections, workoutRoutine
from sqlalchemy import text

"""with SessionLocal.begin() as session:
    workout1 = workouts(Name="Beginner Workout", Description="Simple movements building strength, stamina, and workout confidence")
    workout2 = workouts(Name="Intermediate Workout", Description="Moderate intensity for improving strength, balance, and endurance")
    workout3 = workouts(Name="Advanced Workout", Description="High-intensity training combining strength, speed, and agility drills")
    workout4 = workouts(Name="Athlete Workout", Description="Performance-focused routines for power, speed, and muscle conditioning")
    workout5 = workouts(Name="Child 6-12 yrs Workout", Description="Fun, playful exercises developing coordination, strength, and endurance")
    workout6 = workouts(Name="Young Adult Workout", Description="Energetic sessions boosting metabolism, strength, and cardiovascular health")
    workout7 = workouts(Name="Midlife Workout", Description="Balanced routines for strength, heart health, and joint stability")
    workout8 = workouts(Name="Senior Workout", Description="Gentle yet effective movements supporting strength, mobility, and balance")
    workout9 = workouts(Name="Recovery rehabilitation Workout", Description="Low-impact exercises for healing, flexibility, and gradual strength return")
    workout10 = workouts(Name="Chronic condition Workout", Description="Safe, adaptive routines for strength, stability, and heart health")
    workout11 = workouts(Name="Post Paturm Workout", Description="Core-strengthening and gentle cardio for post-birth recovery fitness")
    workout12 = workouts(Name="Antenatal Workout", Description="Prenatal-safe exercises promoting strength, posture, and heart health")
    workout13 = workouts(Name="Sustainable weight care Workout", Description="Holistic training to support healthy, lasting weight and fitness")
    workout14 = workouts(Name="Accessible fitness Workout", Description="Inclusive workouts adaptable to all needs and ability levels")
    workout15 = workouts(Name="Time constrained  Workout", Description="Quick, high-efficiency circuits to boost strength and burn calories")
    workout16 = workouts(Name="Home based Workout", Description="At-home bodyweight workouts for strength, cardio, and flexibility")
    workout17 = workouts(Name="Minimal Equipment Workout", Description="Creative strength and cardio using basic tools or bodyweight")
    workout18 = workouts(Name="Outdoor Training  Workout", Description="Nature-based workouts blending movement, endurance, and fresh air")
    workout19 = workouts(Name="Gym Equipment Workout", Description="Structured strength and cardio using standard gym machines effectively")
    workout20 = workouts(Name="Weightloss Workout", Description="Fat-burning circuits to increase metabolism and support healthy weight")
    workout21 = workouts(Name="Endurance Workout", Description="Long-duration exercises building stamina, lung capacity, and heart strength")
    workout22 = workouts(Name="Flexibility and mobility Workout", Description="Stretching and movement to improve range, posture, and joint health")
    workout23 = workouts(Name="Everyday movement Workout", Description="Functional training for easier, stronger daily life movements")
    workout24 = workouts(Name="Reducing fall risk Workout", Description="Balance, strength, and reaction exercises to prevent accidental falls")
    workout25 = workouts(Name="Power training  Workout", Description="Explosive movements to boost strength, speed, and athletic performance")
    workout26 = workouts(Name="HIIT Workout", Description="Fast-paced intervals of cardio and strength for quick results")
    workout27 = workouts(Name="Mind and Body Workout", Description="Calming, flowing routines blending strength, breath, and mental focus")
    workout28 = workouts(Name="Agility Workout", Description="Quick footwork and directional drills to improve coordination and speed")
    workout29 = workouts(Name="Isometric Training Workout", Description="Static holds that build strength, stability, and muscle endurance")
    workout30 = workouts(Name="Strength Training Workout", Description="Progressive resistance workouts to build muscle and body power")
    
    session.add_all([workout1, workout2, workout3, workout4, workout5, workout6, workout7, workout8, workout9, workout10, workout11, workout12, workout13, workout14, workout15, workout16, workout17, workout18, workout19, workout20, workout21, workout22, workout23, workout24, workout25, workout26, workout27, workout28, workout29, workout30])
"""

"""with SessionLocal.begin() as session:
    beginner = session.query(workouts).filter_by(Name="Beginner Workout").first()
    intermediate = session.query(workouts).filter_by(Name="Intermediate Workout").first()
    advanced = session.query(workouts).filter_by(Name="Advanced Workout").first()
    athlete = session.query(workouts).filter_by(Name="Athlete Workout").first()
    child = session.query(workouts).filter_by(Name="Child 6-12 yrs Workout").first()
    young_adult = session.query(workouts).filter_by(Name="Young Adult Workout").first()
    midlife = session.query(workouts).filter_by(Name="Midlife Workout").first()
    senior = session.query(workouts).filter_by(Name="Senior Workout").first()
    recovery_rehabilitation = session.query(workouts).filter_by(Name="Recovery rehabilitation Workout").first()
    chronic_condition = session.query(workouts).filter_by(Name="Chronic condition Workout").first()
    post_partum = session.query(workouts).filter_by(Name="Post Paturm Workout").first()
    antenatal = session.query(workouts).filter_by(Name="Antenatal Workout").first()
    sustainable_weight_care = session.query(workouts).filter_by(Name="Sustainable weight care Workout").first()
    accessible_fitness = session.query(workouts).filter_by(Name="Accessible fitness Workout").first()
    time_constrained = session.query(workouts).filter_by(Name="Time constrained  Workout").first()
    home_based = session.query(workouts).filter_by(Name="Home based Workout").first()
    minimal_equipment = session.query(workouts).filter_by(Name="Minimal Equipment Workout").first()
    outdoor = session.query(workouts).filter_by(Name="Outdoor Training  Workout").first()
    gym_equipment = session.query(workouts).filter_by(Name="Gym Equipment Workout").first()
    weightloss = session.query(workouts).filter_by(Name="Weightloss Workout").first()
    endurance = session.query(workouts).filter_by(Name="Endurance Workout").first()
    flexibility_mobility = session.query(workouts).filter_by(Name="Flexibility and mobility Workout").first()
    everyday_movement = session.query(workouts).filter_by(Name="Everyday movement Workout").first()
    reducing_fall_risk = session.query(workouts).filter_by(Name="Reducing fall risk Workout").first()
    power_training = session.query(workouts).filter_by(Name="Power training  Workout").first()
    hiit = session.query(workouts).filter_by(Name="HIIT Workout").first()
    mind_and_body = session.query(workouts).filter_by(Name="Mind and Body Workout").first()
    agility = session.query(workouts).filter_by(Name="Agility Workout").first()
    isometric = session.query(workouts).filter_by(Name="Isometric Training Workout").first()
    strength = session.query(workouts).filter_by(Name="Strength Training Workout").first()
    
    sections = [
        workout_sections(SectionName="Beginner Warm Up", SectionOrder=1, T2=beginner),
        workout_sections(SectionName="Beginner Circuit", SectionOrder=2, T2=beginner),
        workout_sections(SectionName="Beginner Cool Down", SectionOrder=3, T2=beginner),
        
        workout_sections(SectionName="Intermediate Warm Up", SectionOrder=1, T2=intermediate),
        workout_sections(SectionName="Intermediate Circuit", SectionOrder=2, T2=intermediate),
        workout_sections(SectionName="Intermediate Cool Down", SectionOrder=3, T2=intermediate),
        
        workout_sections(SectionName="Advanced Warm Up", SectionOrder=1, T2=advanced),
        workout_sections(SectionName="Advanced Circuit", SectionOrder=2, T2=advanced),
        workout_sections(SectionName="Advanced Cool Down", SectionOrder=3, T2=advanced),
        
        workout_sections(SectionName="Athlete Warm Up", SectionOrder=1, T2=athlete),
        workout_sections(SectionName="Athlete Circuit", SectionOrder=2, T2=athlete),
        workout_sections(SectionName="Athlete Cool Down", SectionOrder=3, T2=athlete),
        
        workout_sections(SectionName="Child Warm Up", SectionOrder=1, T2=child),
        workout_sections(SectionName="Child Circuit", SectionOrder=2, T2=child),
        workout_sections(SectionName="Child Cool Down", SectionOrder=3, T2=child),
        
        workout_sections(SectionName="Young Adult Warm Up", SectionOrder=1, T2=young_adult),
        workout_sections(SectionName="Young Adult Circuit", SectionOrder=2, T2=young_adult),
        workout_sections(SectionName="Young Adult Cool Down", SectionOrder=3, T2=young_adult),
        
        workout_sections(SectionName="Midlife Warm Up", SectionOrder=1, T2=midlife),
        workout_sections(SectionName="Midlife Circuit", SectionOrder=2, T2=midlife),
        workout_sections(SectionName="Midlife Cool Down", SectionOrder=3, T2=midlife),
        
        workout_sections(SectionName="Senior Warm Up", SectionOrder=1, T2=senior),
        workout_sections(SectionName="Senior Circuit", SectionOrder=2, T2=senior),
        workout_sections(SectionName="Senior Cool Down", SectionOrder=3, T2=senior),
        
        workout_sections(SectionName="Recovery rehabilitation Warm Up", SectionOrder=1, T2=recovery_rehabilitation),
        workout_sections(SectionName="Recovery rehabilitation Circuit", SectionOrder=2, T2=recovery_rehabilitation),
        workout_sections(SectionName="Recovery rehabilitation Cool Down", SectionOrder=3, T2=recovery_rehabilitation),
        
        workout_sections(SectionName="Chronic condition Warm Up", SectionOrder=1, T2=chronic_condition),
        workout_sections(SectionName="Chronic condition Circuit", SectionOrder=2, T2=chronic_condition),
        workout_sections(SectionName="Chronic condition Cool Down", SectionOrder=3, T2=chronic_condition),
        
        workout_sections(SectionName="Post Partum Warm Up", SectionOrder=1, T2=post_partum),
        workout_sections(SectionName="Post Partum Circuit", SectionOrder=2, T2=post_partum),
        workout_sections(SectionName="Post Partum Cool Down", SectionOrder=3, T2=post_partum),
        
        workout_sections(SectionName="Antenatal Warm Up", SectionOrder=1, T2=antenatal),
        workout_sections(SectionName="Antenatal Circuit", SectionOrder=2, T2=antenatal),
        workout_sections(SectionName="Antenatal Cool Down", SectionOrder=3, T2=antenatal),
        
        workout_sections(SectionName="Sustainable Weight Care Warm Up", SectionOrder=1, T2=sustainable_weight_care),
        workout_sections(SectionName="Sustainable Weight Care Circuit", SectionOrder=2, T2=sustainable_weight_care),
        workout_sections(SectionName="Sustainable Weight Care Cool Down", SectionOrder=3, T2=sustainable_weight_care),
        
        workout_sections(SectionName="Accessible fitness Warm Up", SectionOrder=1, T2=accessible_fitness),
        workout_sections(SectionName="Accessible fitness Circuit", SectionOrder=2, T2=accessible_fitness),
        workout_sections(SectionName="Accessible fitness Cool Down", SectionOrder=3, T2=accessible_fitness),
        
        workout_sections(SectionName="Time constrained Warm Up", SectionOrder=1, T2=time_constrained),
        workout_sections(SectionName="Time constrained Circuit", SectionOrder=2, T2=time_constrained),
        workout_sections(SectionName="Time constrained Cool Down", SectionOrder=3, T2=time_constrained),
        
        workout_sections(SectionName="Home based Warm Up", SectionOrder=1, T2=home_based),
        workout_sections(SectionName="Home based Circuit", SectionOrder=2, T2=home_based),
        workout_sections(SectionName="Home based Cool Down", SectionOrder=3, T2=home_based),
        
        workout_sections(SectionName="Minimal Equipment Warm Up", SectionOrder=1, T2=minimal_equipment),
        workout_sections(SectionName="Minimal Equipment Circuit", SectionOrder=2, T2=minimal_equipment),
        workout_sections(SectionName="Minimal Equipment Cool Down", SectionOrder=3, T2=minimal_equipment),
        
        workout_sections(SectionName="Outdoor Training Warm Up", SectionOrder=1, T2=outdoor),
        workout_sections(SectionName="Outdoor Training Circuit", SectionOrder=2, T2=outdoor),
        workout_sections(SectionName="Outdoor Training Cool Down", SectionOrder=3, T2=outdoor),
        
        workout_sections(SectionName="Gym Equipment Warm Up", SectionOrder=1, T2=gym_equipment),
        workout_sections(SectionName="Gym Equipment Circuit", SectionOrder=2, T2=gym_equipment),
        workout_sections(SectionName="Gym Equipment Cool Down", SectionOrder=3, T2=gym_equipment),
        
        workout_sections(SectionName="Weightloss Warm Up", SectionOrder=1, T2=weightloss),
        workout_sections(SectionName="Weightloss Circuit", SectionOrder=2, T2=weightloss),
        workout_sections(SectionName="Weightloss Cool Down", SectionOrder=3, T2=weightloss),
        
        workout_sections(SectionName="Endurance Warm Up", SectionOrder=1, T2=endurance),
        workout_sections(SectionName="Endurance Circuit", SectionOrder=2, T2=endurance),
        workout_sections(SectionName="Endurance Cool Down", SectionOrder=3, T2=endurance),
        
        workout_sections(SectionName="Flexibility and Mobility Warm Up", SectionOrder=1, T2=flexibility_mobility),
        workout_sections(SectionName="Flexibility and Mobility Circuit", SectionOrder=2, T2=flexibility_mobility),
        workout_sections(SectionName="Flexibility and Mobility Cool Down", SectionOrder=3, T2=flexibility_mobility),
        
        workout_sections(SectionName="Everyday Movement Warm Up", SectionOrder=1, T2=everyday_movement),
        workout_sections(SectionName="Everyday Movement Circuit", SectionOrder=2, T2=everyday_movement),
        workout_sections(SectionName="Everyday Movement Cool Down", SectionOrder=3, T2=everyday_movement),
        
        workout_sections(SectionName="Reducing Fall Warm Up", SectionOrder=1, T2=reducing_fall_risk),
        workout_sections(SectionName="Reducing Fall Circuit", SectionOrder=2, T2=reducing_fall_risk),
        workout_sections(SectionName="Reducing Fall Cool Down", SectionOrder=3, T2=reducing_fall_risk),
        
        workout_sections(SectionName="Power Training Warm Up", SectionOrder=1, T2=power_training),
        workout_sections(SectionName="Power Training Circuit", SectionOrder=2, T2=power_training),
        workout_sections(SectionName="Power Training Cool Down", SectionOrder=3, T2=power_training),
        
        workout_sections(SectionName="HIIT Warm Up", SectionOrder=1, T2=hiit),
        workout_sections(SectionName="HIIT Circuit", SectionOrder=2, T2=hiit),
        workout_sections(SectionName="HIIT Cool Down", SectionOrder=3, T2=hiit),
        
        workout_sections(SectionName="Mind and Body Warm Up", SectionOrder=1, T2=mind_and_body),
        workout_sections(SectionName="Mind and Body Circuit", SectionOrder=2, T2=mind_and_body),
        workout_sections(SectionName="Mind and Body Cool Down", SectionOrder=3, T2=mind_and_body),
        
        workout_sections(SectionName="Agility Warm Up", SectionOrder=1, T2=agility),
        workout_sections(SectionName="Agility Circuit", SectionOrder=2, T2=agility),
        workout_sections(SectionName="Agility Cool Down", SectionOrder=3, T2=agility),
        
        workout_sections(SectionName="Isometric Training Warm Up", SectionOrder=1, T2=isometric),
        workout_sections(SectionName="Isometric Training Circuit", SectionOrder=2, T2=isometric),
        workout_sections(SectionName="Isometric Training Cool Down", SectionOrder=3, T2=isometric),
        
        workout_sections(SectionName="Strength Training Warm Up", SectionOrder=1, T2=strength),
        workout_sections(SectionName="Strength Training Circuit", SectionOrder=2, T2=strength),
        workout_sections(SectionName="Strength Training Cool Down", SectionOrder=3, T2=strength),
    ]
    
    session.add_all(sections)
    
with SessionLocal.begin() as session:
    beginner_warmup = session.query(workout_sections).filter_by(SectionName="Beginner Warm Up").first()
    beginner_circuit = session.query(workout_sections).filter_by(SectionName="Beginner Circuit").first()
    beginner_cooldown = session.query(workout_sections).filter_by(SectionName="Beginner Cool Down").first()
    
    beginner_section = [
        #Warm up
        workoutRoutine(Name="Arm Circles", RepsDuration="Repeat twice", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=1, SectionID=beginner_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="10 reps", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=2, SectionID=beginner_warmup.ID),
        workoutRoutine(Name="Lunges", RepsDuration="5 reps each leg", RoutineDescription="Alternate legs. Step forward, lower knee, push back up", ExerciseOrder=3, SectionID=beginner_warmup.ID),
        workoutRoutine(Name="Jumping Jacks", RepsDuration="30 seconds", RoutineDescription="Jump, spread legs, raise arms, return repeatedly", ExerciseOrder=4, SectionID=beginner_warmup.ID),
        workoutRoutine(Name="Plank hold", RepsDuration="20 seconds", RoutineDescription="Keep body straight, engage core, hold position", ExerciseOrder=5, SectionID=beginner_warmup.ID),
        
        #Circuit
        workoutRoutine(Name="Goblet Squats", RepsDuration="10-12 reps", RoutineDescription="Hold weight at chest, squat down, rise", ExerciseOrder=6, SectionID=beginner_circuit.ID),
        workoutRoutine(Name="Push ups", RepsDuration="8-10 reps", RoutineDescription="Modify by doing them on knees if needed", ExerciseOrder=7, SectionID=beginner_circuit.ID),
        workoutRoutine(Name="Dumbbell Deadlifts", RepsDuration="10 reps", RoutineDescription="Hinge hips, lower dumbbells, stand up strong", ExerciseOrder=8, SectionID=beginner_circuit.ID),
        workoutRoutine(Name="Bent-Over Rows", RepsDuration="10 reps", RoutineDescription="Hinge forward, pull weights to torso, lower slowly", ExerciseOrder=9, SectionID=beginner_circuit.ID),
        workoutRoutine(Name="Glute Bridges", RepsDuration="10-12 reps", RoutineDescription="Lift hips, squeeze glutes, lower back down", ExerciseOrder=10, SectionID=beginner_circuit.ID),
        workoutRoutine(Name="Shoulder Press", RepsDuration="8-10 reps", RoutineDescription="Use light dumbbells. Press weights overhead, extend arms, lower controlled", ExerciseOrder=11, SectionID=beginner_circuit.ID),
        workoutRoutine(Name="Plank Shoulder Taps", RepsDuration="10 reps per side", RoutineDescription="Hold plank, tap shoulders alternately.", ExerciseOrder=12, SectionID=beginner_circuit.ID),
        workoutRoutine(Name="Russian Twists", RepsDuration="10 reps per side", RoutineDescription="Bodyweight or Dumbbell. Sit, twist torso side to side, engage core", ExerciseOrder=13, SectionID=beginner_circuit.ID),
        
        #Cool down
        workoutRoutine(Name="Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=14, SectionID=beginner_cooldown.ID),
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Seated Forward Fold", ExerciseOrder=15, SectionID=beginner_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=16, SectionID=beginner_cooldown.ID),
        workoutRoutine(Name="Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=17, SectionID=beginner_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=beginner_cooldown.ID)
    ]
    session.add_all(beginner_section)
    
    intermediate_warmup = session.query(workout_sections).filter_by(SectionName="Intermediate Warm Up").first()
    intermediate_circuit = session.query(workout_sections).filter_by(SectionName="Intermediate Circuit").first()
    intermediate_cooldown = session.query(workout_sections).filter_by(SectionName="Intermediate Cool Down").first()
    
    intermediate_section = [
        #Warm up
        workoutRoutine(Name="Jump rope", RepsDuration="30 seconds", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=intermediate_warmup.ID),
        workoutRoutine(Name="Arm Circles", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=intermediate_warmup.ID),
        workoutRoutine(Name="Leg Swings", RepsDuration="30 seconds", RoutineDescription="Front & Side 30 seconds each", ExerciseOrder=3, SectionID=intermediate_warmup.ID),
        workoutRoutine(Name="Inchworms to Push-up", RepsDuration="30 seconds", RoutineDescription="Walk hands forward, do push-up, return standing", ExerciseOrder=4, SectionID=intermediate_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="30 seconds", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=5, SectionID=intermediate_warmup.ID),

        #Circuit
        workoutRoutine(Name="Jump Squats", RepsDuration="40s, rest 20s", RoutineDescription="Squat down, explode up, land softly, repeat", ExerciseOrder=6, SectionID=intermediate_circuit.ID),
        workoutRoutine(Name="Push-ups to Shoulder Taps", RepsDuration="40s, rest 20s", RoutineDescription="Perform push-up, tap opposite shoulder, alternate sides", ExerciseOrder=7, SectionID=intermediate_circuit.ID),
        workoutRoutine(Name="Dumbbell Lunges", RepsDuration="40s, rest 20s", RoutineDescription="Alternate legs. Step forward, lower knee, push back up. Add weights on each arm", ExerciseOrder=8, SectionID=intermediate_circuit.ID),
        workoutRoutine(Name="Mountain Climbers", RepsDuration="40s, rest 20s", RoutineDescription="Run knees toward chest in a plank position", ExerciseOrder=9, SectionID=intermediate_circuit.ID),
        workoutRoutine(Name="Dumbbell Deadlifts to Bent-over Row", RepsDuration="40s, rest 20s", RoutineDescription="Hinge down, lift dumbbells, row, lower back", ExerciseOrder=10, SectionID=intermediate_circuit.ID),
        workoutRoutine(Name="Plank to Knee Tucks", RepsDuration="40s, rest 20s", RoutineDescription="Hold plank, drive knees toward chest, alternate sides", ExerciseOrder=11, SectionID=intermediate_circuit.ID),
        workoutRoutine(Name="Kettlebell Swings", RepsDuration="40s, rest 20s", RoutineDescription="Hinge hips, swing kettlebell up, control down", ExerciseOrder=12, SectionID=intermediate_circuit.ID),
        workoutRoutine(Name="Burpees", RepsDuration="40s, rest 20s", RoutineDescription="Squat, jump back, push-up, jump up explosively", ExerciseOrder=13, SectionID=intermediate_circuit.ID),

        #Cool down
        workoutRoutine(Name="Childs Pose", RepsDuration="30 seconds", RoutineDescription="Kneel, stretch arms forward, relax back", ExerciseOrder=14, SectionID=intermediate_cooldown.ID),
        workoutRoutine(Name="Seated Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Sit, extend legs, reach toward toes, hold stretch. 30 seconds per leg", ExerciseOrder=15, SectionID=intermediate_cooldown.ID),
        workoutRoutine(Name="Hip Flexor Stretch", RepsDuration="30 seconds", RoutineDescription="Lunge forward, press hips down, stretch deeply", ExerciseOrder=16, SectionID=intermediate_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=17, SectionID=intermediate_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=intermediate_cooldown.ID),
    ]
    session.add_all(intermediate_section)
    
    advanced_warmup = session.query(workout_sections).filter_by(SectionName="Advanced Warm Up").first()
    advanced_circuit = session.query(workout_sections).filter_by(SectionName="Advanced Circuit").first()
    advanced_cooldown = session.query(workout_sections).filter_by(SectionName="Advanced Cool Down").first()
    
    advanced_section = [
        #Warm up
        workoutRoutine(Name="Jump rope", RepsDuration="45 seconds", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=advanced_warmup.ID),
        workoutRoutine(Name="Worlds Greatest Stretch", RepsDuration="45 seconds", RoutineDescription="Lunge forward, rotate torso, reach arm upward 30 seconds each side", ExerciseOrder=2, SectionID=advanced_warmup.ID),
        workoutRoutine(Name="Lateral Lunges with Arm Swings", RepsDuration="45 seconds", RoutineDescription="Step sideways, lunge down, swing arms dynamically", ExerciseOrder=3, SectionID=advanced_warmup.ID),
        workoutRoutine(Name="Inchworm to Push-up", RepsDuration="45 seconds", RoutineDescription="Walk hands forward, do push-up, return standing", ExerciseOrder=4, SectionID=advanced_warmup.ID),
        workoutRoutine(Name="Explosive Bodyweight Squats", RepsDuration="45 seconds", RoutineDescription="Squat down, jump up, land softly", ExerciseOrder=5, SectionID=advanced_warmup.ID),

        #Circuit
        workoutRoutine(Name="Dumbbell Thrusters", RepsDuration="45s, rest 15s", RoutineDescription="Squat down, press dumbbells overhead explosively, repeat", ExerciseOrder=6, SectionID=advanced_circuit.ID),
        workoutRoutine(Name="Jump Lunges", RepsDuration="45s, rest 15s", RoutineDescription="or Weighted Jump Lunges. Lunge down, jump up, switch legs mid-air", ExerciseOrder=7, SectionID=advanced_circuit.ID),
        workoutRoutine(Name="Pull-ups", RepsDuration="45s, rest 15s", RoutineDescription="Hang from a bar, pull chin above it", ExerciseOrder=8, SectionID=advanced_circuit.ID),
        workoutRoutine(Name="Box Jumps to Burpee", RepsDuration="45s, rest 15s", RoutineDescription="Jump onto box, step down, perform burpee, repeat", ExerciseOrder=9, SectionID=advanced_circuit.ID),
        workoutRoutine(Name="Deadlift to Bent-over Row", RepsDuration="45s, rest 15s", RoutineDescription="Hinge down, lift weights, row at bottom, stand up", ExerciseOrder=10, SectionID=advanced_circuit.ID),
        workoutRoutine(Name="Spiderman Push-ups", RepsDuration="45s, rest 15s", RoutineDescription="Lower body, bring knee to elbow, switch sides", ExerciseOrder=11, SectionID=advanced_circuit.ID),
        workoutRoutine(Name="Kettlebell Swings", RepsDuration="45s, rest 15s", RoutineDescription="Hinge hips, swing kettlebell up, control down", ExerciseOrder=12, SectionID=advanced_circuit.ID),
        workoutRoutine(Name="Battle Ropes", RepsDuration="45s, rest 15s", RoutineDescription="Grip ropes, create waves, slams, or circular motions", ExerciseOrder=13, SectionID=advanced_circuit.ID),

        #Cool down
        workoutRoutine(Name="Downward Dog", RepsDuration="40 seconds", RoutineDescription="Lift hips, straighten legs, press heels down", ExerciseOrder=14, SectionID=advanced_cooldown.ID),
        workoutRoutine(Name="Pigeon Pose", RepsDuration="40 seconds", RoutineDescription="30 sec per side. Extend one leg back, fold front leg forward", ExerciseOrder=15, SectionID=advanced_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="40 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=16, SectionID=advanced_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="40 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=17, SectionID=advanced_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=advanced_cooldown.ID),
    ]
    session.add_all(advanced_section)

    athlete_warmup = session.query(workout_sections).filter_by(SectionName="Athlete Warm Up").first()
    athlete_circuit = session.query(workout_sections).filter_by(SectionName="Athlete Circuit").first()
    athlete_cooldown = session.query(workout_sections).filter_by(SectionName="Athlete Cool Down").first()

    athlete_section = [
        
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="45 seconds", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=athlete_warmup.ID),
        workoutRoutine(Name="Worlds Greatest Stretch", RepsDuration="45 seconds", RoutineDescription="Lunge forward, rotate torso, reach arm upward 30 seconds each side", ExerciseOrder=2, SectionID=athlete_warmup.ID),
        workoutRoutine(Name="A-Skips", RepsDuration="45 seconds", RoutineDescription="Skip forward, drive knees high, swing arms dynamically", ExerciseOrder=3, SectionID=athlete_warmup.ID),
        workoutRoutine(Name="Lateral Bounds", RepsDuration="45 seconds", RoutineDescription="Jump side to side, land softly, maintain balance", ExerciseOrder=4, SectionID=athlete_warmup.ID),
        workoutRoutine(Name="Depth Jumps to Sprint", RepsDuration="45 seconds", RoutineDescription="Short 5-Yard Burst. Step off box, land, explode into sprint immediately", ExerciseOrder=5, SectionID=athlete_warmup.ID),

        #Circuit
        workoutRoutine(Name="Power Cleans", RepsDuration="45s, rest 15s", RoutineDescription="Lift barbell explosively from floor to shoulders", ExerciseOrder=6, SectionID=athlete_circuit.ID),
        workoutRoutine(Name="Sprint Intervals", RepsDuration="45s, rest 15s", RoutineDescription="Sprint for 30 yards", ExerciseOrder=7, SectionID=athlete_circuit.ID),
        workoutRoutine(Name="Bulgarian Split Squats", RepsDuration="45s, rest 15s", RoutineDescription="Elevate back foot, lower into lunge, push up", ExerciseOrder=8, SectionID=athlete_circuit.ID),
        workoutRoutine(Name="Pull-ups", RepsDuration="45s, rest 15s", RoutineDescription="Hang from a bar, pull chin above it", ExerciseOrder=9, SectionID=athlete_circuit.ID),
        workoutRoutine(Name="Box Jumps", RepsDuration="45s, rest 15s", RoutineDescription="Jump onto box, land softly, stand tall", ExerciseOrder=10, SectionID=athlete_circuit.ID),
        workoutRoutine(Name="Sled Push", RepsDuration="45s, rest 15s", RoutineDescription="Drive sled forward, engage legs, maintain low posture", ExerciseOrder=11, SectionID=athlete_circuit.ID),
        workoutRoutine(Name="Plank-to-Explosive Knee Drive", RepsDuration="45s, rest 15s", RoutineDescription="Hold plank, drive knee forward quickly, switch sides", ExerciseOrder=12, SectionID=athlete_circuit.ID),
        workoutRoutine(Name="Med Ball Slams", RepsDuration="45s, rest 15s", RoutineDescription="Lift medicine ball overhead, slam it down forcefully", ExerciseOrder=13, SectionID=athlete_circuit.ID),

        #Cool down
        workoutRoutine(Name="Couch Stretch", RepsDuration="40 seconds", RoutineDescription="Rest foot on surface, lunge forward, stretch quads", ExerciseOrder=14, SectionID=athlete_cooldown.ID),
        workoutRoutine(Name="Thoracic Spine Rotation Stretch", RepsDuration="40 seconds", RoutineDescription="Rotate upper body, reach arm upward, open chest", ExerciseOrder=15, SectionID=athlete_cooldown.ID),
        workoutRoutine(Name="Pigeon Pose", RepsDuration="40 seconds", RoutineDescription="30 sec per side. Extend one leg back, fold front leg forward", ExerciseOrder=16, SectionID=athlete_cooldown.ID),
        workoutRoutine(Name="Hamstring & Calf Stretch", RepsDuration="40 seconds", RoutineDescription="Extend leg, hinge forward, flex foot, hold stretch", ExerciseOrder=17, SectionID=athlete_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=athlete_cooldown.ID),
    ]
    session.add_all(athlete_section)
    
    child_warmup = session.query(workout_sections).filter_by(SectionName="Child Warm Up").first()
    child_circuit = session.query(workout_sections).filter_by(SectionName="Child Circuit").first()
    child_cooldown = session.query(workout_sections).filter_by(SectionName="Child Cool Down").first()

    child_section = [
        
        #Warm up
        workoutRoutine(Name="Jumping Jacks", RepsDuration="20 seconds", RoutineDescription="Jump, spread legs, raise arms, return repeatedly", ExerciseOrder=1, SectionID=child_warmup.ID),
        workoutRoutine(Name="Arm Circles", RepsDuration="20 seconds", RoutineDescription="20 seconds forward, 20 seconds backward. Rotate arms in small or large circular motions", ExerciseOrder=2, SectionID=child_warmup.ID),
        workoutRoutine(Name="Marching High Knees", RepsDuration="20 seconds", RoutineDescription="Lift knees high, engage core, move rhythmically", ExerciseOrder=3, SectionID=child_warmup.ID),
        workoutRoutine(Name="Bear Crawls", RepsDuration="20 seconds", RoutineDescription="Crawl forward on hands and feet, keep low", ExerciseOrder=4, SectionID=child_warmup.ID),
        workoutRoutine(Name="Frog Jumps", RepsDuration="20 seconds", RoutineDescription="Squat low, jump forward, land softly, repeat", ExerciseOrder=5, SectionID=child_warmup.ID),

        #Circuit
        workoutRoutine(Name="Crab walk", RepsDuration="20s, rest 20s", RoutineDescription="Sit, lift hips, walk backward and forward using hands and feet", ExerciseOrder=6, SectionID=child_circuit.ID),
        workoutRoutine(Name="Superhero Hold", RepsDuration="20s, rest 20s", RoutineDescription="Lie face down, lift arms and legs, hold position", ExerciseOrder=7, SectionID=child_circuit.ID),
        workoutRoutine(Name="Squat Jumps", RepsDuration="20s, rest 20s", RoutineDescription="Squat down, explode up, land softly, repeat", ExerciseOrder=8, SectionID=child_circuit.ID),
        workoutRoutine(Name="Push-ups", RepsDuration="20s, rest 20s", RoutineDescription="Knees Allowed if needed", ExerciseOrder=9, SectionID=child_circuit.ID),
        workoutRoutine(Name="Fast Feet", RepsDuration="20s, rest 20s", RoutineDescription="Like Running in Place on Hot Lava", ExerciseOrder=10, SectionID=child_circuit.ID),
        workoutRoutine(Name="Balance Hold", RepsDuration="20s, rest 20s", RoutineDescription="One-Leg Stand", ExerciseOrder=11, SectionID=child_circuit.ID),
        workoutRoutine(Name="Freeze Dance", RepsDuration="20s, rest 20s", RoutineDescription="Dance and Stop on Command", ExerciseOrder=12, SectionID=child_circuit.ID),
        workoutRoutine(Name="Bunny Hops", RepsDuration="20s, rest 20s", RoutineDescription="Jump forward repeatedly with feet together, stay low", ExerciseOrder=13, SectionID=child_circuit.ID),

        #Cool down
        workoutRoutine(Name="Butterfly Stretch", RepsDuration="30 seconds", RoutineDescription="Sit, press soles together, gently push knees down", ExerciseOrder=14, SectionID=child_cooldown.ID),
        workoutRoutine(Name="Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=15, SectionID=child_cooldown.ID),
        workoutRoutine(Name="Toe Touch Stretch", RepsDuration="30 seconds", RoutineDescription="Stand or sit, reach forward, touch toes, hold", ExerciseOrder=16, SectionID=child_cooldown.ID),
        workoutRoutine(Name="Big Arm Stretches", RepsDuration="30 seconds", RoutineDescription="Hug Yourself", ExerciseOrder=17, SectionID=child_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="30 seconds", RoutineDescription="Blow Out Like a Birthday Candle", ExerciseOrder=18, SectionID=child_cooldown.ID),
    ]
    session.add_all(child_section)

    youngadult_warmup = session.query(workout_sections).filter_by(SectionName="Young Adult Warm Up").first()
    youngadult_circuit = session.query(workout_sections).filter_by(SectionName="Young Adult Circuit").first()
    youngadult_cooldown = session.query(workout_sections).filter_by(SectionName="Young Adult Cool Down").first()

    youngadult_section = [
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="30 seconds", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=youngadult_warmup.ID),
        workoutRoutine(Name="Leg Swings", RepsDuration="30 seconds", RoutineDescription="Front & Side 30 seconds each", ExerciseOrder=2, SectionID=youngadult_warmup.ID),
        workoutRoutine(Name="Arm Circles", RepsDuration="30 seconds", RoutineDescription="30 seconds forward, 30 seconds backward. Rotate arms in small or large circular motions", ExerciseOrder=3, SectionID=youngadult_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats to Calf Raise", RepsDuration="30 seconds", RoutineDescription="Squat down, stand up, lift heels", ExerciseOrder=4, SectionID=youngadult_warmup.ID),
        workoutRoutine(Name="Inchworms to Push-up", RepsDuration="30 seconds", RoutineDescription="Walk hands forward, do push-up, return standing", ExerciseOrder=5, SectionID=youngadult_warmup.ID),

        #Circuit
        workoutRoutine(Name="Jump Squats", RepsDuration="40s, rest 20s", RoutineDescription="Squat down, explode up, land softly, repeat", ExerciseOrder=6, SectionID=youngadult_circuit.ID),
        workoutRoutine(Name="Push-ups to Shoulder Taps", RepsDuration="40s, rest 20s", RoutineDescription="Perform push-up, tap opposite shoulder, alternate sides", ExerciseOrder=7, SectionID=youngadult_circuit.ID),
        workoutRoutine(Name="Dumbbell Reverse Lunges", RepsDuration="40s, rest 20s", RoutineDescription="Step back, lower knee, push up holding dumbbells", ExerciseOrder=8, SectionID=youngadult_circuit.ID),
        workoutRoutine(Name="Mountain Climbers", RepsDuration="40s, rest 20s", RoutineDescription="Run knees toward chest in a plank position", ExerciseOrder=9, SectionID=youngadult_circuit.ID),
        workoutRoutine(Name="Deadlifts to Bent-over Row", RepsDuration="40s, rest 20s", RoutineDescription="Hinge down, lift weights, row, lower, stand up", ExerciseOrder=10, SectionID=youngadult_circuit.ID),
        workoutRoutine(Name="Plank to Knee Tucks", RepsDuration="40s, rest 20s", RoutineDescription="Hold plank, drive knees toward chest, alternate sides", ExerciseOrder=11, SectionID=youngadult_circuit.ID),
        workoutRoutine(Name="Kettlebell Swings", RepsDuration="40s, rest 20s", RoutineDescription="Hinge hips, swing kettlebell up, control down", ExerciseOrder=12, SectionID=youngadult_circuit.ID),
        workoutRoutine(Name="Burpees", RepsDuration="40s, rest 20s", RoutineDescription="Squat, jump back, push-up, jump up explosively", ExerciseOrder=13, SectionID=youngadult_circuit.ID),

        #Cool down
        workoutRoutine(Name="Childs Pose", RepsDuration="40 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=14, SectionID=youngadult_cooldown.ID),
        workoutRoutine(Name="Hip Flexor Stretch", RepsDuration="40 seconds", RoutineDescription="Lunge forward, press hips down, stretch deeply", ExerciseOrder=15, SectionID=youngadult_cooldown.ID),
        workoutRoutine(Name="Seated Hamstring Stretch", RepsDuration="40 seconds", RoutineDescription="Sit, extend legs, reach toward toes, hold stretch. 30 seconds per leg", ExerciseOrder=16, SectionID=youngadult_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="40 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=17, SectionID=youngadult_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=youngadult_cooldown.ID),
    ]
    session.add_all(youngadult_section)
    
    midlife_warmup = session.query(workout_sections).filter_by(SectionName="Midlife Warm Up").first()
    midlife_circuit = session.query(workout_sections).filter_by(SectionName="Midlife Circuit").first()
    midlife_cooldown = session.query(workout_sections).filter_by(SectionName="Midlife Cool Down").first()

    midlife_section = [
        #Warm up
        workoutRoutine(Name="March in Place with Arm Swings", RepsDuration="30 seconds", RoutineDescription="Lift knees, swing arms rhythmically, engage core", ExerciseOrder=1, SectionID=midlife_warmup.ID),
        workoutRoutine(Name="Shoulder Rolls & Neck Stretches", RepsDuration="30 seconds", RoutineDescription="Roll shoulders forward and backward, then gently tilt the head side to side", ExerciseOrder=2, SectionID=midlife_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats to Heel Raise", RepsDuration="30 seconds", RoutineDescription="Squat down, stand up, lift heels", ExerciseOrder=3, SectionID=midlife_warmup.ID),
        workoutRoutine(Name="Standing Leg Swings", RepsDuration="30 seconds", RoutineDescription="Front & Side 30 seconds each leg", ExerciseOrder=4, SectionID=midlife_warmup.ID),
        workoutRoutine(Name="Cat-Cow Stretch", RepsDuration="30 seconds", RoutineDescription="Arch and round back, flow between positions smoothly", ExerciseOrder=5, SectionID=midlife_warmup.ID),

        #Circuit
        workoutRoutine(Name="Step-ups", RepsDuration="35 secs, 20s rest", RoutineDescription="Step onto platform, drive through heel, switch legs", ExerciseOrder=6, SectionID=midlife_circuit.ID),
        workoutRoutine(Name="Push-ups", RepsDuration="35 secs, 20s rest", RoutineDescription="Lower chest to floor, push up, keep core engaged", ExerciseOrder=7, SectionID=midlife_circuit.ID),
        workoutRoutine(Name="Standing Dumbbell Shoulder Press", RepsDuration="35 secs, 20s rest", RoutineDescription="Can be seated as well. Press weights overhead, extend arms, lower controlled", ExerciseOrder=8, SectionID=midlife_circuit.ID),
        workoutRoutine(Name="Standing Rows", RepsDuration="35 secs, 20s rest", RoutineDescription="Pull weights toward chest, keep back straight, control movement", ExerciseOrder=9, SectionID=midlife_circuit.ID),
        workoutRoutine(Name="Glute Bridges", RepsDuration="35 secs, 20s rest", RoutineDescription="Lift hips, squeeze glutes, lower back down", ExerciseOrder=10, SectionID=midlife_circuit.ID),
        workoutRoutine(Name="Side-to-Side Step Touches", RepsDuration="35 secs, 20s rest", RoutineDescription="Step sideways, touch floor or tap opposite foot", ExerciseOrder=11, SectionID=midlife_circuit.ID),
        workoutRoutine(Name="Plank hold", RepsDuration="35 secs, 20s rest", RoutineDescription="Keep body straight, engage core, hold position", ExerciseOrder=12, SectionID=midlife_circuit.ID),
        workoutRoutine(Name="Farmers Walk", RepsDuration="35 secs, 20s rest", RoutineDescription="Carry heavy weights, walk upright, engage core", ExerciseOrder=13, SectionID=midlife_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Sit, extend legs, reach toward toes, hold stretch. 30 seconds per leg", ExerciseOrder=14, SectionID=midlife_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=15, SectionID=midlife_cooldown.ID),
        workoutRoutine(Name="Seated Figure-Four Stretch", RepsDuration="30 seconds", RoutineDescription="Sit, cross ankle over knee, lean forward gently", ExerciseOrder=16, SectionID=midlife_cooldown.ID),
        workoutRoutine(Name="Childs Pose", RepsDuration="30 seconds", RoutineDescription="hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=17, SectionID=midlife_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=midlife_cooldown.ID),
    ]
    session.add_all(midlife_section)

    senior_warmup = session.query(workout_sections).filter_by(SectionName="Senior Warm Up").first()
    senior_circuit = session.query(workout_sections).filter_by(SectionName="Senior Circuit").first()
    senior_cooldown = session.query(workout_sections).filter_by(SectionName="Senior Cool Down").first()

    senior_section = [
        #Warm up
        workoutRoutine(Name="Neck & Shoulder Rolls", RepsDuration="40 seconds", RoutineDescription="Roll shoulders forward and backward, then slowly rotate the neck side to side", ExerciseOrder=1, SectionID=senior_warmup.ID),
        workoutRoutine(Name="Seated or Standing March", RepsDuration="40 seconds", RoutineDescription="Lightly march in place, swinging arms", ExerciseOrder=2, SectionID=senior_warmup.ID),
        workoutRoutine(Name="Torso Twists", RepsDuration="40 seconds", RoutineDescription="Stand or sit and rotate the torso gently from side to side", ExerciseOrder=3, SectionID=senior_warmup.ID),
        workoutRoutine(Name="Heel & Toe Taps", RepsDuration="40 seconds", RoutineDescription="Alternate tapping heels and toes, engage legs and balance", ExerciseOrder=4, SectionID=senior_warmup.ID),
        workoutRoutine(Name="Arm Circles", RepsDuration="40 seconds", RoutineDescription="30 seconds forward, 30 seconds backward. Rotate arms in small or large circular motions", ExerciseOrder=5, SectionID=senior_warmup.ID),

        #Circuit
        workoutRoutine(Name="Chair Squats", RepsDuration="10 reps, 30s rest", RoutineDescription="Sit back onto chair, stand up, engage core", ExerciseOrder=6, SectionID=senior_circuit.ID),
        workoutRoutine(Name="Seated Knee Lifts", RepsDuration="10 reps per side", RoutineDescription="Sit on a chair, lift knees alternately, engaging the core", ExerciseOrder=7, SectionID=senior_circuit.ID),
        workoutRoutine(Name="Wall Push-Ups", RepsDuration="10 reps, 30s rest", RoutineDescription="Lean into wall, lower chest, push back up", ExerciseOrder=8, SectionID=senior_circuit.ID),
        workoutRoutine(Name="Side Step with Arm Reach", RepsDuration="35 secs, 20s rest", RoutineDescription="Step sideways, extend arm overhead, engage core", ExerciseOrder=9, SectionID=senior_circuit.ID),
        workoutRoutine(Name="Standing Bicep Curls", RepsDuration="10 reps per side", RoutineDescription="Curl weights upward, squeeze biceps, lower controlled.", ExerciseOrder=10, SectionID=senior_circuit.ID),
        workoutRoutine(Name="Toe Taps to Elevated Surface", RepsDuration="35 secs, 20s rest", RoutineDescription="Tap toes alternately on platform, maintain steady rhythm", ExerciseOrder=11, SectionID=senior_circuit.ID),
        workoutRoutine(Name="Standing Leg Raises", RepsDuration="10 reps per side", RoutineDescription="Lift leg forward or sideways, keep core engaged", ExerciseOrder=12, SectionID=senior_circuit.ID),
        workoutRoutine(Name="Seated Overhead Press", RepsDuration="10 reps, 30s rest", RoutineDescription="Press weights overhead, keep back straight, lower controlled", ExerciseOrder=13, SectionID=senior_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Bend", RepsDuration="30 seconds", RoutineDescription="Sit, extend legs, reach forward, stretch hamstrings", ExerciseOrder=14, SectionID=senior_cooldown.ID),
        workoutRoutine(Name="Chest Stretch", RepsDuration="30 seconds", RoutineDescription="Open arms wide, pull shoulders back, expand chest", ExerciseOrder=15, SectionID=senior_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=senior_cooldown.ID),
        workoutRoutine(Name="Ankle & Wrist Rolls", RepsDuration="30 seconds", RoutineDescription="Rotate ankles and wrists in controlled rolls", ExerciseOrder=17, SectionID=senior_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=senior_cooldown.ID),
    ]
    
    session.add_all(senior_section)

    recovery_warmup = session.query(workout_sections).filter_by(SectionName="Recovery rehabilitation Warm Up").first()
    recovery_circuit = session.query(workout_sections).filter_by(SectionName="Recovery rehabilitation Circuit").first()
    recovery_cooldown = session.query(workout_sections).filter_by(SectionName="Recovery rehabilitation Cool Down").first()

    recovery_section = [
        #Warm up
        workoutRoutine(Name="Deep Breathing & Arm Reaches", RepsDuration="40 seconds", RoutineDescription="Inhale while raising arms overhead, exhale while lowering", ExerciseOrder=1, SectionID=recovery_warmup.ID),
        workoutRoutine(Name="Standing Shoulder Rolls", RepsDuration="40 seconds", RoutineDescription="Roll shoulders forward and backward, keep movements controlled", ExerciseOrder=2, SectionID=recovery_warmup.ID),
        workoutRoutine(Name="Standing Heel & Toe Taps", RepsDuration="40 seconds", RoutineDescription="Alternate tapping heels and toes while maintaining balance", ExerciseOrder=3, SectionID=recovery_warmup.ID),
        workoutRoutine(Name="Standing Side Bends", RepsDuration="40 seconds", RoutineDescription="Stand tall, bend sideways, stretch obliques, repeat", ExerciseOrder=4, SectionID=recovery_warmup.ID),
        workoutRoutine(Name="Gentle Neck Rotations", RepsDuration="40 seconds", RoutineDescription="Slowly rotate neck in full, gentle circles", ExerciseOrder=5, SectionID=recovery_warmup.ID),

        #Circuit
        workoutRoutine(Name="Standing Leg Raises", RepsDuration="10 reps, 30s rest", RoutineDescription="Lift leg forward or sideways, keep core engaged", ExerciseOrder=6, SectionID=recovery_circuit.ID),
        workoutRoutine(Name="Heel Raises", RepsDuration="10 reps, 30s rest", RoutineDescription="Lift heels, balance on toes, lower down", ExerciseOrder=7, SectionID=recovery_circuit.ID),
        workoutRoutine(Name="Standing Marches", RepsDuration="10 reps, 30s rest", RoutineDescription="Stand upright, lift knees in rhythmic marches", ExerciseOrder=8, SectionID=recovery_circuit.ID),
        workoutRoutine(Name="Wall Push-Ups", RepsDuration="10 reps, 30s rest", RoutineDescription="Lean into wall, lower chest, push back up", ExerciseOrder=9, SectionID=recovery_circuit.ID),
        workoutRoutine(Name="Standing Side Leg Raises", RepsDuration="10 reps, 30s rest", RoutineDescription="Stand tall, lift leg sideways, lower steadily", ExerciseOrder=10, SectionID=recovery_circuit.ID),
        workoutRoutine(Name="Step Touch Side-to-Side", RepsDuration="10 reps, 30s rest", RoutineDescription="Step gently side to side while moving arms", ExerciseOrder=11, SectionID=recovery_circuit.ID),
        workoutRoutine(Name="Chair Squats", RepsDuration="10 reps, 30s rest", RoutineDescription="Sit back onto chair, stand up, engage core", ExerciseOrder=12, SectionID=recovery_circuit.ID),
        workoutRoutine(Name="Standing Arm Circles", RepsDuration="10 reps, 30s rest", RoutineDescription="30 seconds forward, 30 seconds backward. Rotate arms in small or large circular motions", ExerciseOrder=13, SectionID=recovery_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Bend", RepsDuration="30 seconds", RoutineDescription="Sit, extend legs, reach forward, stretch hamstrings", ExerciseOrder=14, SectionID=recovery_cooldown.ID),
        workoutRoutine(Name="Chest Stretch", RepsDuration="30 seconds", RoutineDescription="Open arms wide, pull shoulders back, expand chest", ExerciseOrder=15, SectionID=recovery_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gentl", ExerciseOrder=16, SectionID=recovery_cooldown.ID),
        workoutRoutine(Name="Ankle & Wrist Rolls", RepsDuration="30 seconds", RoutineDescription="Rotate ankles and wrists in controlled rolls", ExerciseOrder=17, SectionID=recovery_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=recovery_cooldown.ID),
    ]

    session.add_all(recovery_section)
    
    chronic_warmup = session.query(workout_sections).filter_by(SectionName="Chronic condition Warm Up").first()
    chronic_circuit = session.query(workout_sections).filter_by(SectionName="Chronic condition Circuit").first()
    chronic_cooldown = session.query(workout_sections).filter_by(SectionName="Chronic condition Cool Down").first()

    chronic_section = [
        #Warm up
        workoutRoutine(Name="Deep Breathing & Arm Reaches", RepsDuration="40 seconds", RoutineDescription="Inhale while raising arms overhead, exhale while lowering", ExerciseOrder=1, SectionID=chronic_warmup.ID),
        workoutRoutine(Name="Standing Shoulder Rolls", RepsDuration="40 seconds", RoutineDescription="Roll shoulders forward and backward, keep movements controlled", ExerciseOrder=2, SectionID=chronic_warmup.ID),
        workoutRoutine(Name="Ankle & Wrist Circles", RepsDuration="40 seconds", RoutineDescription="Rotate ankles and wrists in controlled circles", ExerciseOrder=3, SectionID=chronic_warmup.ID),
        workoutRoutine(Name="Standing Side Bends", RepsDuration="40 seconds", RoutineDescription="Stand tall, lean sideways, stretch obliques, repeat", ExerciseOrder=4, SectionID=chronic_warmup.ID),
        workoutRoutine(Name="Heel & Toe Taps", RepsDuration="40 seconds", RoutineDescription="Alternate tapping heels and toes, engage legs and balance", ExerciseOrder=5, SectionID=chronic_warmup.ID),

        #Circuit
        workoutRoutine(Name="Standing Marches", RepsDuration="10 reps, 30s rest", RoutineDescription="Stand upright, lift knees in rhythmic marches", ExerciseOrder=6, SectionID=chronic_circuit.ID),
        workoutRoutine(Name="Chair Squats", RepsDuration="10 reps, 30s rest", RoutineDescription="Sit back onto chair, stand up, engage core", ExerciseOrder=7, SectionID=chronic_circuit.ID),
        workoutRoutine(Name="Standing Bicep Curls", RepsDuration="10 reps, 30s rest", RoutineDescription="Curl weights upward, squeeze biceps, lower controlled", ExerciseOrder=8, SectionID=chronic_circuit.ID),
        workoutRoutine(Name="Side Step Touches", RepsDuration="10 reps, 30s rest", RoutineDescription="Step sideways, tap foot, alternate with rhythm", ExerciseOrder=9, SectionID=chronic_circuit.ID),
        workoutRoutine(Name="Heel Raises", RepsDuration="10 reps, 30s rest", RoutineDescription="Lift heels, balance on toes, lower down", ExerciseOrder=10, SectionID=chronic_circuit.ID),
        workoutRoutine(Name="Overhead Press", RepsDuration="10 reps, 30s rest", RoutineDescription="Press weights overhead, extend arms, lower steadily", ExerciseOrder=11, SectionID=chronic_circuit.ID),
        workoutRoutine(Name="Standing Leg Extensions", RepsDuration="10 reps, 30s rest", RoutineDescription="Stand tall, extend leg forward, lower steadily", ExerciseOrder=12, SectionID=chronic_circuit.ID),
        workoutRoutine(Name="Step Touch with Arm Swings", RepsDuration="10 reps, 30s rest", RoutineDescription="Step sideways, tap foot, swing arms rhythmically", ExerciseOrder=13, SectionID=chronic_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Bend", RepsDuration="30 seconds", RoutineDescription="Sit, extend legs, reach forward, stretch hamstrings", ExerciseOrder=14, SectionID=chronic_cooldown.ID),
        workoutRoutine(Name="Chest Stretch", RepsDuration="30 seconds", RoutineDescription="Open arms wide, pull shoulders back, expand chest", ExerciseOrder=15, SectionID=chronic_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=chronic_cooldown.ID),
        workoutRoutine(Name="Neck stretches", RepsDuration="30 seconds", RoutineDescription="Tilt head side to side and forward", ExerciseOrder=17, SectionID=chronic_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=chronic_cooldown.ID),
    ]

    session.add_all(chronic_section)
    
    postpartum_warmup = session.query(workout_sections).filter_by(SectionName="Post Partum Warm Up").first()
    postpartum_circuit = session.query(workout_sections).filter_by(SectionName="Post Partum Circuit").first()
    postpartum_cooldown = session.query(workout_sections).filter_by(SectionName="Post Partum Cool Down").first()

    postpartum_section = [
        #Warm up
        workoutRoutine(Name="Deep Breathing with Core", RepsDuration="35 seconds", RoutineDescription="Inhale deeply, expand the belly, then exhale while drawing the navel toward the spine to activate the core", ExerciseOrder=1, SectionID=postpartum_warmup.ID),
        workoutRoutine(Name="Pelvic Tilts", RepsDuration="35 seconds", RoutineDescription="Tilt pelvis forward and backward, engage core", ExerciseOrder=2, SectionID=postpartum_warmup.ID),
        workoutRoutine(Name="Neck & Shoulder Rolls", RepsDuration="35 seconds", RoutineDescription="Gently rotate neck and shoulders, easing tension", ExerciseOrder=3, SectionID=postpartum_warmup.ID),
        workoutRoutine(Name="Standing Marches", RepsDuration="35 seconds", RoutineDescription="Stand upright, lift knees in rhythmic marches", ExerciseOrder=4, SectionID=postpartum_warmup.ID),
        workoutRoutine(Name="Side-to-Side Toe Taps", RepsDuration="35 seconds", RoutineDescription="Step sideways, tap toes, alternate, maintain balance", ExerciseOrder=5, SectionID=postpartum_warmup.ID),

        #Circuit
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="35 secs, 30s rest", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=6, SectionID=postpartum_circuit.ID),
        workoutRoutine(Name="Glute Bridges", RepsDuration="35 secs, 30s rest", RoutineDescription="Lift hips, squeeze glutes, lower back down", ExerciseOrder=7, SectionID=postpartum_circuit.ID),
        workoutRoutine(Name="Modified Push-Ups", RepsDuration="35 secs, 30s rest", RoutineDescription="Gently perform push-ups on knees for support", ExerciseOrder=8, SectionID=postpartum_circuit.ID),
        workoutRoutine(Name="Standing Overhead Press", RepsDuration="35 secs, 30s rest", RoutineDescription="Stand upright, press weights overhead, lower slowly", ExerciseOrder=9, SectionID=postpartum_circuit.ID),
        workoutRoutine(Name="Side-Lying Leg Lifts", RepsDuration="35 secs, 30s rest", RoutineDescription="Lie on side, lift leg, lower slowly", ExerciseOrder=10, SectionID=postpartum_circuit.ID),
        workoutRoutine(Name="Standing Step Back Lunges", RepsDuration="35 secs, 30s rest", RoutineDescription="Step backward, lower knee, return to standing", ExerciseOrder=11, SectionID=postpartum_circuit.ID),
        workoutRoutine(Name="Standing Bicep Curls", RepsDuration="35 secs, 30s rest", RoutineDescription="Curl weights upward, squeeze biceps, lower controlled", ExerciseOrder=12, SectionID=postpartum_circuit.ID),
        workoutRoutine(Name="Standing March with Arm Swings", RepsDuration="35 secs, 30s rest", RoutineDescription="Stand, march in place, swing arms dynamically", ExerciseOrder=13, SectionID=postpartum_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=14, SectionID=postpartum_cooldown.ID),
        workoutRoutine(Name="Chest Stretch", RepsDuration="30 seconds", RoutineDescription="Open arms wide, pull shoulders back, expand chest", ExerciseOrder=15, SectionID=postpartum_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=postpartum_cooldown.ID),
        workoutRoutine(Name="Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=17, SectionID=postpartum_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=postpartum_cooldown.ID),
    ]

    session.add_all(postpartum_section)
    
    antenatal_warmup = session.query(workout_sections).filter_by(SectionName="Antenatal Warm Up").first()
    antenatal_circuit = session.query(workout_sections).filter_by(SectionName="Antenatal Circuit").first()
    antenatal_cooldown = session.query(workout_sections).filter_by(SectionName="Antenatal Cool Down").first()

    antenatal_section = [
        #Warm up
        workoutRoutine(Name="Deep Breathing with Core", RepsDuration="35 seconds", RoutineDescription="Inhale deeply, expand the belly, then exhale while drawing the navel toward the spine to activate the core", ExerciseOrder=1, SectionID=antenatal_warmup.ID),
        workoutRoutine(Name="Pelvic Tilts", RepsDuration="35 seconds", RoutineDescription="Tilt pelvis forward and backward, engage core", ExerciseOrder=2, SectionID=antenatal_warmup.ID),
        workoutRoutine(Name="Side-to-Side Sway with Arm Swings", RepsDuration="35 seconds", RoutineDescription="Sway side-to-side, swing arms in rhythmic motion", ExerciseOrder=3, SectionID=antenatal_warmup.ID),
        workoutRoutine(Name="Neck & Shoulder Rolls", RepsDuration="35 seconds", RoutineDescription="Gently rotate neck and shoulders, easing tension", ExerciseOrder=4, SectionID=antenatal_warmup.ID),
        workoutRoutine(Name="Standing Marches", RepsDuration="35 seconds", RoutineDescription="Stand upright, lift knees in rhythmic marches", ExerciseOrder=5, SectionID=antenatal_warmup.ID),

        #Circuit
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="35 secs, 30s rest", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=6, SectionID=antenatal_circuit.ID),
        workoutRoutine(Name="Standing Bicep Curls", RepsDuration="35 secs, 30s rest", RoutineDescription="Curl weights upward, squeeze biceps, lower controlled", ExerciseOrder=7, SectionID=antenatal_circuit.ID),
        workoutRoutine(Name="Standing Side Leg Raises", RepsDuration="35 secs, 30s rest", RoutineDescription="Stand tall, lift leg sideways, lower steadily", ExerciseOrder=8, SectionID=antenatal_circuit.ID),
        workoutRoutine(Name="Wall Push-Ups", RepsDuration="35 secs, 30s rest", RoutineDescription="Lean into wall, lower chest, push back up", ExerciseOrder=9, SectionID=antenatal_circuit.ID),
        workoutRoutine(Name="Side Step Touch with Arm Reaches", RepsDuration="35 secs, 30s rest", RoutineDescription="Step sideways, touch foot, reach arms upward", ExerciseOrder=10, SectionID=antenatal_circuit.ID),
        workoutRoutine(Name="Glute Bridges", RepsDuration="35 secs, 30s rest", RoutineDescription="Lift hips, squeeze glutes, lower back down", ExerciseOrder=11, SectionID=antenatal_circuit.ID),
        workoutRoutine(Name="Standing Overhead Press", RepsDuration="35 secs, 30s rest", RoutineDescription="Stand upright, press weights overhead, lower slowly", ExerciseOrder=12, SectionID=antenatal_circuit.ID),
        workoutRoutine(Name="Gentle Step Backs with Arm Swings", RepsDuration="35 secs, 30s rest", RoutineDescription="Step one foot back at a time while swinging arms forward", ExerciseOrder=13, SectionID=antenatal_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=14, SectionID=antenatal_cooldown.ID),
        workoutRoutine(Name="Chest Stretch", RepsDuration="30 seconds", RoutineDescription="Open arms wide, pull shoulders back, expand chest", ExerciseOrder=15, SectionID=antenatal_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=antenatal_cooldown.ID),
        workoutRoutine(Name="Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=17, SectionID=antenatal_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=antenatal_cooldown.ID),
    ]

    session.add_all(antenatal_section)
    
    sustainable_warmup = session.query(workout_sections).filter_by(SectionName="Sustainable Weight Care Warm Up").first()
    sustainable_circuit = session.query(workout_sections).filter_by(SectionName="Sustainable Weight Care Circuit").first()
    sustainable_cooldown = session.query(workout_sections).filter_by(SectionName="Sustainable Weight Care Cool Down").first()

    sustainable_section = [
        #Warm up
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="35 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=1, SectionID=sustainable_warmup.ID),
        workoutRoutine(Name="Torso Twists", RepsDuration="35 seconds", RoutineDescription="Rotate torso side-to-side, engaging your core muscles", ExerciseOrder=2, SectionID=sustainable_warmup.ID),
        workoutRoutine(Name="High Knees", RepsDuration="35 seconds", RoutineDescription="Low or High Impact - March or jog in place", ExerciseOrder=3, SectionID=sustainable_warmup.ID),
        workoutRoutine(Name="Bodyweight Good Mornings", RepsDuration="35 seconds", RoutineDescription="Hinge at the hips with a straight back and return to standing", ExerciseOrder=4, SectionID=sustainable_warmup.ID),
        workoutRoutine(Name="Step Touch with Arm Swings", RepsDuration="35 seconds", RoutineDescription="Step sideways, tap foot, swing arms rhythmically", ExerciseOrder=5, SectionID=sustainable_warmup.ID),

        #Circuit
        workoutRoutine(Name="Squats", RepsDuration="12 reps", RoutineDescription="Lower hips, bend knees, then stand up", ExerciseOrder=6, SectionID=sustainable_circuit.ID),
        workoutRoutine(Name="Push-Ups", RepsDuration="12 reps", RoutineDescription="Lower chest to floor, push up, keep core engaged", ExerciseOrder=7, SectionID=sustainable_circuit.ID),
        workoutRoutine(Name="Jump Rope", RepsDuration="12 reps", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=8, SectionID=sustainable_circuit.ID),
        workoutRoutine(Name="Lunges", RepsDuration="12 reps", RoutineDescription="Alternate legs. Step forward, lower knee, push back up", ExerciseOrder=9, SectionID=sustainable_circuit.ID),
        workoutRoutine(Name="Bent-Over Rows", RepsDuration="12 reps", RoutineDescription="Hinge forward, pull weights to chest, lower slowly", ExerciseOrder=10, SectionID=sustainable_circuit.ID),
        workoutRoutine(Name="Overhead Dumbbell Press", RepsDuration="12 reps", RoutineDescription="Press dumbbells overhead, extend arms, lower slowly", ExerciseOrder=11, SectionID=sustainable_circuit.ID),
        workoutRoutine(Name="Mountain Climbers", RepsDuration="35 seconds", RoutineDescription="Run knees toward chest in a plank position", ExerciseOrder=12, SectionID=sustainable_circuit.ID),
        workoutRoutine(Name="Russian Twists", RepsDuration="35 seconds", RoutineDescription="Bodyweight or Dumbbell. Sit, twist torso side to side, engage core", ExerciseOrder=13, SectionID=sustainable_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stand tall, fold forward, stretch hamstrings completely", ExerciseOrder=14, SectionID=sustainable_cooldown.ID),
        workoutRoutine(Name="Chest & Shoulder Stretch", RepsDuration="30 seconds", RoutineDescription="Pull shoulders back, open chest, feel stretch", ExerciseOrder=15, SectionID=sustainable_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=sustainable_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=17, SectionID=sustainable_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=sustainable_cooldown.ID),
    ]

    session.add_all(sustainable_section)
    
    accessible_warmup = session.query(workout_sections).filter_by(SectionName="Accessible fitness Warm Up").first()
    accessible_circuit = session.query(workout_sections).filter_by(SectionName="Accessible fitness Circuit").first()
    accessible_cooldown = session.query(workout_sections).filter_by(SectionName="Accessible fitness Cool Down").first()

    accessible_section = [
        #Warm up
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="35 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=1, SectionID=accessible_warmup.ID),
        workoutRoutine(Name="Shoulder Rolls & Neck Stretches", RepsDuration="35 seconds", RoutineDescription="Roll shoulders forward and backward, then gently tilt the head side to side", ExerciseOrder=2, SectionID=accessible_warmup.ID),
        workoutRoutine(Name="Standing Marches", RepsDuration="35 seconds", RoutineDescription="Stand upright, lift knees in rhythmic marches", ExerciseOrder=3, SectionID=accessible_warmup.ID),
        workoutRoutine(Name="Wrist & Ankle Circles", RepsDuration="35 seconds", RoutineDescription="Rotate wrists and ankles in controlled circles", ExerciseOrder=4, SectionID=accessible_warmup.ID),
        workoutRoutine(Name="Side-to-Side Sway with Arm Swings", RepsDuration="35 seconds", RoutineDescription="Sway side-to-side, swing arms in rhythmic motion", ExerciseOrder=5, SectionID=accessible_warmup.ID),

        #Circuit
        workoutRoutine(Name="Standing Leg Extensions", RepsDuration="35 secs, 30s rest", RoutineDescription="Stand tall, extend leg forward, lower steadily", ExerciseOrder=6, SectionID=accessible_circuit.ID),
        workoutRoutine(Name="Standing Bicep Curls", RepsDuration="35 secs, 30s rest", RoutineDescription="Curl weights upward, squeeze biceps, lower controlled", ExerciseOrder=7, SectionID=accessible_circuit.ID),
        workoutRoutine(Name="Standing Side Leg Raises", RepsDuration="35 secs, 30s rest", RoutineDescription="Stand tall, lift leg sideways, lower steadily", ExerciseOrder=8, SectionID=accessible_circuit.ID),
        workoutRoutine(Name="Wall Push-Ups", RepsDuration="35 secs, 30s rest", RoutineDescription="Lean into wall, lower chest, push back up", ExerciseOrder=9, SectionID=accessible_circuit.ID),
        workoutRoutine(Name="Step Touch with Arm Reaches", RepsDuration="35 secs, 30s rest", RoutineDescription="Step sideways, tap foot, extend arms overhead", ExerciseOrder=10, SectionID=accessible_circuit.ID),
        workoutRoutine(Name="Standing Glute Squeeze", RepsDuration="35 secs, 30s rest", RoutineDescription="Stand tall, squeeze glutes, hold, release", ExerciseOrder=11, SectionID=accessible_circuit.ID),
        workoutRoutine(Name="Overhead Press", RepsDuration="35 secs, 30s rest", RoutineDescription="Press weights overhead, extend arms, lower steadily", ExerciseOrder=12, SectionID=accessible_circuit.ID),
        workoutRoutine(Name="Gentle Step Backs with Arm Swings", RepsDuration="35 secs, 30s rest", RoutineDescription="Step one foot back at a time while swinging arms forward", ExerciseOrder=13, SectionID=accessible_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stand tall, fold forward, stretch hamstrings completely", ExerciseOrder=14, SectionID=accessible_cooldown.ID),
        workoutRoutine(Name="Chest Stretch", RepsDuration="30 seconds", RoutineDescription="Open arms wide, pull shoulders back, expand chest", ExerciseOrder=15, SectionID=accessible_cooldown.ID),
        workoutRoutine(Name="Standing Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Stand tall, twist torso, engage core, hold stretch", ExerciseOrder=16, SectionID=accessible_cooldown.ID),
        workoutRoutine(Name="Standing Ankle Rolls", RepsDuration="30 seconds", RoutineDescription="Stand, lift foot, roll ankle in circles", ExerciseOrder=17, SectionID=accessible_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=accessible_cooldown.ID),
    ]

    session.add_all(accessible_section)
    
    time_warmup = session.query(workout_sections).filter_by(SectionName="Time constrained Warm Up").first()
    time_circuit = session.query(workout_sections).filter_by(SectionName="Time constrained Circuit").first()
    time_cooldown = session.query(workout_sections).filter_by(SectionName="Time constrained Cool Down").first()

    time_constrained_section = [
        #Warm up
        workoutRoutine(Name="Jumping Jacks", RepsDuration="30 seconds", RoutineDescription="or Low-Impact Side Taps. Jump, spread legs, raise arms, return repeatedly", ExerciseOrder=1, SectionID=time_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=time_warmup.ID),
        workoutRoutine(Name="High Knees", RepsDuration="30 seconds", RoutineDescription="Lift knees rapidly while running in place", ExerciseOrder=3, SectionID=time_warmup.ID),
        workoutRoutine(Name="Hip Circles & Torso Twists", RepsDuration="30 seconds", RoutineDescription="Rotate torso and hips for dynamic mobility", ExerciseOrder=4, SectionID=time_warmup.ID),
        workoutRoutine(Name="Squat-to-Stand Stretch", RepsDuration="30 seconds", RoutineDescription="Squat low, stand up, stretch hamstrings deeply", ExerciseOrder=5, SectionID=time_warmup.ID),

        #Circuit
        workoutRoutine(Name="Squat to Shoulder Press", RepsDuration="40 secs, 30s rest", RoutineDescription="Press weights overhead, extend arms, lower controlled", ExerciseOrder=6, SectionID=time_circuit.ID),
        workoutRoutine(Name="Push-Ups", RepsDuration="40 secs, 30s rest", RoutineDescription="Lower chest to floor, push up, keep core engaged", ExerciseOrder=7, SectionID=time_circuit.ID),
        workoutRoutine(Name="Jump Rope", RepsDuration="40 secs, 30s rest", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=8, SectionID=time_circuit.ID),
        workoutRoutine(Name="Lunges", RepsDuration="40 secs, 30s rest", RoutineDescription="Alternate legs. Step forward, lower knee, push back up", ExerciseOrder=9, SectionID=time_circuit.ID),
        workoutRoutine(Name="Bent-Over Rows", RepsDuration="40 secs, 30s rest", RoutineDescription="Hinge forward, pull weights to chest, lower slowly", ExerciseOrder=10, SectionID=time_circuit.ID),
        workoutRoutine(Name="Mountain Climbers", RepsDuration="40 secs, 30s rest", RoutineDescription="Run knees toward chest in a plank position", ExerciseOrder=11, SectionID=time_circuit.ID),
        workoutRoutine(Name="Glute Bridges", RepsDuration="40 secs, 30s rest", RoutineDescription="Lift hips, squeeze glutes, lower back down", ExerciseOrder=12, SectionID=time_circuit.ID),
        workoutRoutine(Name="Plank Hold", RepsDuration="40 secs, 30s rest", RoutineDescription="Keep body straight, engage core, hold position", ExerciseOrder=13, SectionID=time_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stand tall, fold forward, stretch hamstrings completely", ExerciseOrder=14, SectionID=time_cooldown.ID),
        workoutRoutine(Name="Chest & Shoulder Stretch", RepsDuration="30 seconds", RoutineDescription="Pull shoulders back, open chest, feel stretch", ExerciseOrder=15, SectionID=time_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=time_cooldown.ID),
        workoutRoutine(Name="Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=17, SectionID=time_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=time_cooldown.ID),
    ]

    session.add_all(time_constrained_section)
    
    home_warmup = session.query(workout_sections).filter_by(SectionName="Home based Warm Up").first()
    home_circuit = session.query(workout_sections).filter_by(SectionName="Home based Circuit").first()
    home_cooldown = session.query(workout_sections).filter_by(SectionName="Home based Cool Down").first()

    home_section = [
        #Warm up
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=1, SectionID=home_warmup.ID),
        workoutRoutine(Name="Torso Twists", RepsDuration="30 seconds", RoutineDescription="Rotate torso slowly, alternate sides, engage core", ExerciseOrder=2, SectionID=home_warmup.ID),
        workoutRoutine(Name="High Knees", RepsDuration="30 seconds", RoutineDescription="Lift knees rapidly while running in place", ExerciseOrder=3, SectionID=home_warmup.ID),
        workoutRoutine(Name="Bodyweight Good Mornings", RepsDuration="30 seconds", RoutineDescription="Hinge at the hips with a straight back and return to standing", ExerciseOrder=4, SectionID=home_warmup.ID),
        workoutRoutine(Name="Step Touch with Arm Swings", RepsDuration="30 seconds", RoutineDescription="Step sideways, tap foot, swing arms rhythmically", ExerciseOrder=5, SectionID=home_warmup.ID),

        #Circuit
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="12 reps", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=6, SectionID=home_circuit.ID),
        workoutRoutine(Name="Push-Ups", RepsDuration="12 reps", RoutineDescription="Lower chest to floor, push up, keep core engaged", ExerciseOrder=7, SectionID=home_circuit.ID),
        workoutRoutine(Name="Jumping Jacks", RepsDuration="12 reps", RoutineDescription="or Low-Impact Side Steps. Jump, spread legs, raise arms, return repeatedly", ExerciseOrder=8, SectionID=home_circuit.ID),
        workoutRoutine(Name="Lunges", RepsDuration="12 reps", RoutineDescription="Alternate legs. Step forward, lower knee, push back up", ExerciseOrder=9, SectionID=home_circuit.ID),
        workoutRoutine(Name="Bent-Over Rows", RepsDuration="12 reps", RoutineDescription="Hinge forward, pull weights to chest, lower slowly", ExerciseOrder=10, SectionID=home_circuit.ID),
        workoutRoutine(Name="Mountain Climbers", RepsDuration="35 secs, 20s rest", RoutineDescription="Run knees toward chest in a plank position", ExerciseOrder=11, SectionID=home_circuit.ID),
        workoutRoutine(Name="Glute Bridges", RepsDuration="35 secs, 20s rest", RoutineDescription="On the Floor or Couch Edge. Lift hips, squeeze glutes, lower back down", ExerciseOrder=12, SectionID=home_circuit.ID),
        workoutRoutine(Name="Plank Hold", RepsDuration="35 secs, 20s rest", RoutineDescription="Keep body straight, engage core, hold position", ExerciseOrder=13, SectionID=home_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stand tall, fold forward, stretch hamstrings completely", ExerciseOrder=14, SectionID=home_cooldown.ID),
        workoutRoutine(Name="Chest & Shoulder Stretch", RepsDuration="30 seconds", RoutineDescription="Pull shoulders back, open chest, feel stretch", ExerciseOrder=15, SectionID=home_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=home_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=17, SectionID=home_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=home_cooldown.ID),
    ]
    session.add_all(home_section)
    
    minimal_warmup = session.query(workout_sections).filter_by(SectionName="Minimal Equipment Warm Up").first()
    minimal_circuit = session.query(workout_sections).filter_by(SectionName="Minimal Equipment Circuit").first()
    minimal_cooldown = session.query(workout_sections).filter_by(SectionName="Minimal Equipment Cool Down").first()
    
    minimal_section = [
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="30 seconds", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=minimal_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=minimal_warmup.ID),
        workoutRoutine(Name="Hip Openers", RepsDuration="30 seconds", RoutineDescription="Gently open hips, improve mobility, relax muscles.", ExerciseOrder=3, SectionID=minimal_warmup.ID),
        workoutRoutine(Name="Bodyweight Good Mornings", RepsDuration="30 seconds", RoutineDescription="Hinge at the hips, keeping the back straight, then return upright", ExerciseOrder=4, SectionID=minimal_warmup.ID),
        workoutRoutine(Name="Side Step with Arm Swings", RepsDuration="30 seconds", RoutineDescription="Step laterally, swing arms rhythmically, maintain balance", ExerciseOrder=5, SectionID=minimal_warmup.ID),

        #Circuit
        workoutRoutine(Name="Goblet Squats", RepsDuration="12 reps", RoutineDescription="Hold weight at chest, squat down, rise", ExerciseOrder=6, SectionID=minimal_circuit.ID),
        workoutRoutine(Name="Dumbbell rows", RepsDuration="12 reps", RoutineDescription="Hinge forward, pull dumbbells to torso, lower", ExerciseOrder=7, SectionID=minimal_circuit.ID),
        workoutRoutine(Name="Jump Rope", RepsDuration="12 reps", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=8, SectionID=minimal_circuit.ID),
        workoutRoutine(Name="Lunges with Dumbbells", RepsDuration="12 reps", RoutineDescription="Step, lower knee, push up holding dumbbells", ExerciseOrder=9, SectionID=minimal_circuit.ID),
        workoutRoutine(Name="Overhead Dumbbell Press", RepsDuration="12 reps", RoutineDescription="Press dumbbells overhead, extend arms, lower slowly", ExerciseOrder=10, SectionID=minimal_circuit.ID),
        workoutRoutine(Name="Dumbbell Swings", RepsDuration="12 reps", RoutineDescription="Hinge hips, swing dumbbell upward, control descent", ExerciseOrder=11, SectionID=minimal_circuit.ID),
        workoutRoutine(Name="Plank to Row", RepsDuration="12 reps", RoutineDescription="Hold plank, row dumbbell, alternate arms steadily", ExerciseOrder=12, SectionID=minimal_circuit.ID),
        workoutRoutine(Name="Bicycle Crunches", RepsDuration="12 reps", RoutineDescription="Lie on back, twist, alternate elbow-to-knee crunches", ExerciseOrder=13, SectionID=minimal_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stand tall, fold forward, stretch hamstrings completely", ExerciseOrder=14, SectionID=minimal_cooldown.ID),
        workoutRoutine(Name="Chest & Shoulder Stretch", RepsDuration="30 seconds", RoutineDescription="Pull shoulders back, open chest, feel stretch", ExerciseOrder=15, SectionID=minimal_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=minimal_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=17, SectionID=minimal_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=minimal_cooldown.ID),
    ]

    session.add_all(minimal_section)
    
    outdoor_warmup = session.query(workout_sections).filter_by(SectionName="Outdoor Training Warm Up").first()
    outdoor_circuit = session.query(workout_sections).filter_by(SectionName="Outdoor Training Circuit").first()
    outdoor_cooldown = session.query(workout_sections).filter_by(SectionName="Outdoor Training Cool Down").first()

    outdoor_section = [
        #Warm up
        workoutRoutine(Name="Brisk Walk", RepsDuration="35 seconds", RoutineDescription="Walk briskly, elevate heart rate,", ExerciseOrder=1, SectionID=outdoor_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="35 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back.", ExerciseOrder=2, SectionID=outdoor_warmup.ID),
        workoutRoutine(Name="Bodyweight Good Mornings", RepsDuration="35 seconds", RoutineDescription="Hinge at the hips, keeping the back straight, and return to standing.", ExerciseOrder=3, SectionID=outdoor_warmup.ID),
        workoutRoutine(Name="Leg Swings", RepsDuration="35 seconds", RoutineDescription="Front & Side 35 seconds each direction", ExerciseOrder=4, SectionID=outdoor_warmup.ID),
        workoutRoutine(Name="Side-to-Side Lunges", RepsDuration="35 seconds", RoutineDescription="Step sideways, bend knee, keep chest up", ExerciseOrder=5, SectionID=outdoor_warmup.ID),

        #Circuit
        workoutRoutine(Name="Park Bench Step-Ups", RepsDuration="12 reps", RoutineDescription="Step onto bench, drive through heel, switch legs.", ExerciseOrder=6, SectionID=outdoor_circuit.ID),
        workoutRoutine(Name="Incline Push-Ups", RepsDuration="12 reps", RoutineDescription="Hands on elevated surface, lower chest, push up.", ExerciseOrder=7, SectionID=outdoor_circuit.ID),
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="12 reps", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=8, SectionID=outdoor_circuit.ID),
        workoutRoutine(Name="Triceps Dips on Bench", RepsDuration="12 reps", RoutineDescription="Bench dip: lower, push up, engage triceps.", ExerciseOrder=9, SectionID=outdoor_circuit.ID),
        workoutRoutine(Name="Lunges", RepsDuration="12 reps", RoutineDescription="Walking or Stationary. Alternate legs. Step forward, lower knee, push back up", ExerciseOrder=10, SectionID=outdoor_circuit.ID),
        workoutRoutine(Name="Bear Crawl", RepsDuration="12 reps", RoutineDescription="Crawl forward on hands and feet, keep low.", ExerciseOrder=11, SectionID=outdoor_circuit.ID),
        workoutRoutine(Name="Sprint", RepsDuration="35 seconds", RoutineDescription="Run fast, drive knees, pump arms explosively.", ExerciseOrder=12, SectionID=outdoor_circuit.ID),
        workoutRoutine(Name="Plank Hold", RepsDuration="35 seconds", RoutineDescription="Keep body straight, engage core, hold position", ExerciseOrder=13, SectionID=outdoor_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Fold on Bench", RepsDuration="30 seconds", RoutineDescription="or do it on the Grass. Stretch hamstrings by reaching toward toes", ExerciseOrder=14, SectionID=outdoor_cooldown.ID),
        workoutRoutine(Name="Chest & Shoulder Stretch", RepsDuration="30 seconds", RoutineDescription="Pull shoulders back, open chest, feel stretch.", ExerciseOrder=15, SectionID=outdoor_cooldown.ID),
        workoutRoutine(Name="Standing Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Stand tall, twist torso, engage core, hold stretch", ExerciseOrder=16, SectionID=outdoor_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=17, SectionID=outdoor_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax.", ExerciseOrder=18, SectionID=outdoor_cooldown.ID),
    ]

    session.add_all(outdoor_section)
    
    gym_warmup = session.query(workout_sections).filter_by(SectionName="Gym Equipment Warm Up").first()
    gym_circuit = session.query(workout_sections).filter_by(SectionName="Gym Equipment Circuit").first()
    gym_cooldown = session.query(workout_sections).filter_by(SectionName="Gym Equipment Cool Down").first()

    gym_section = [
        #Warm up
        workoutRoutine(Name="Treadmill Walk", RepsDuration="35 seconds", RoutineDescription="Walk on treadmill, elevate heartrate", ExerciseOrder=1, SectionID=gym_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="35 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=gym_warmup.ID),
        workoutRoutine(Name="Leg Swings", RepsDuration="35 seconds", RoutineDescription="Front & Side. 35 seconds each direction", ExerciseOrder=3, SectionID=gym_warmup.ID),
        workoutRoutine(Name="Bodyweight Good Mornings", RepsDuration="35 seconds", RoutineDescription="Hinge at the hips with a straight back and return to standing", ExerciseOrder=4, SectionID=gym_warmup.ID),
        workoutRoutine(Name="Seated Torso Twists", RepsDuration="35 seconds", RoutineDescription="Sit tall, rotate torso side to side", ExerciseOrder=5, SectionID=gym_warmup.ID),

        #Circuit
        workoutRoutine(Name="Leg Press Machine", RepsDuration="12 reps", RoutineDescription="Adjust the seat, press through heels, and extend your legs", ExerciseOrder=6, SectionID=gym_circuit.ID),
        workoutRoutine(Name="Lat Pulldown Machine", RepsDuration="12 reps", RoutineDescription="Pull the bar down toward your chest, keeping elbows tucked", ExerciseOrder=7, SectionID=gym_circuit.ID),
        workoutRoutine(Name="Treadmill Sprints", RepsDuration="40 secs, 30s rest", RoutineDescription="Run fast, drive knees, pump arms explosively", ExerciseOrder=8, SectionID=gym_circuit.ID),
        workoutRoutine(Name="Dumbbell Lunges", RepsDuration="12 reps", RoutineDescription="Walking or Stationary each side. Step forward, lower knee, hold dumbbells steadily", ExerciseOrder=9, SectionID=gym_circuit.ID),
        workoutRoutine(Name="Dumbbell Shoulder Press", RepsDuration="12 reps", RoutineDescription="Press weights overhead, extend arms, lower controlled", ExerciseOrder=10, SectionID=gym_circuit.ID),
        workoutRoutine(Name="Dumbbell Bent-Over Rows", RepsDuration="12 reps", RoutineDescription="Hinge forward, row dumbbells to chest, lower", ExerciseOrder=11, SectionID=gym_circuit.ID),
        workoutRoutine(Name="Incline Treadmill Walk", RepsDuration="40 secs, 30s rest", RoutineDescription="Walk uphill, engage legs, boost endurance gradually", ExerciseOrder=12, SectionID=gym_circuit.ID),
        workoutRoutine(Name="Weighted Plank", RepsDuration="40 secs, 30s rest", RoutineDescription="Hold plank with added weight, engage core tightly", ExerciseOrder=13, SectionID=gym_circuit.ID),

        #Cool down
        workoutRoutine(Name="Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="on a Bench or Machine. Extend one leg forward and reach for your toes", ExerciseOrder=14, SectionID=gym_cooldown.ID),
        workoutRoutine(Name="Chest Stretch Using a wall", RepsDuration="30 seconds", RoutineDescription="Open arms wide, pull shoulders back, expand chest", ExerciseOrder=15, SectionID=gym_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit on a bench and twist gently to each side", ExerciseOrder=16, SectionID=gym_cooldown.ID),
        workoutRoutine(Name="Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Using a Machine for Support - Hold one foot behind to stretch the front of the thigh", ExerciseOrder=17, SectionID=gym_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=gym_cooldown.ID),
    ]

    session.add_all(gym_section)
    
    weightloss_warmup = session.query(workout_sections).filter_by(SectionName="Weightloss Warm Up").first()
    weightloss_circuit = session.query(workout_sections).filter_by(SectionName="Weightloss Circuit").first()
    weightloss_cooldown = session.query(workout_sections).filter_by(SectionName="Weightloss Cool Down").first()

    weightloss_section = [
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="35 seconds", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=weightloss_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="35 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=weightloss_warmup.ID),
        workoutRoutine(Name="Torso Twists", RepsDuration="35 seconds", RoutineDescription="Rotate side to side to engage the core", ExerciseOrder=3, SectionID=weightloss_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="35 seconds", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=4, SectionID=weightloss_warmup.ID),
        workoutRoutine(Name="Side Step with Arm Swings", RepsDuration="35 seconds", RoutineDescription="Step side to side while moving arms forward and back", ExerciseOrder=5, SectionID=weightloss_warmup.ID),

        #Circuit
        workoutRoutine(Name="Squat to Shoulder Press", RepsDuration="10 reps", RoutineDescription="Use Dumbbells or Bodyweight. Squat down and press overhead when standing", ExerciseOrder=6, SectionID=weightloss_circuit.ID),
        workoutRoutine(Name="Jump Squats", RepsDuration="10 reps", RoutineDescription="Low-Impact Option: Bodyweight Squats. Explode upward or focus on controlled squats", ExerciseOrder=7, SectionID=weightloss_circuit.ID),
        workoutRoutine(Name="Push-Ups", RepsDuration="10 reps", RoutineDescription="Lower chest to floor, push up, keep core engaged", ExerciseOrder=8, SectionID=weightloss_circuit.ID),
        workoutRoutine(Name="Lunges with Dumbbells", RepsDuration="10 reps", RoutineDescription="Or Bodyweight. Walking or Stationary each side. Step forward, lower knee, hold dumbbells steadily", ExerciseOrder=9, SectionID=weightloss_circuit.ID),
        workoutRoutine(Name="Burpees", RepsDuration="30 secs, 20s rest", RoutineDescription="Squat, jump back, push-up, jump up explosively", ExerciseOrder=10, SectionID=weightloss_circuit.ID),
        workoutRoutine(Name="Dumbbell Bent-Over Rows", RepsDuration="10 reps", RoutineDescription="Hinge forward, pull dumbbells to torso, lower slowly", ExerciseOrder=11, SectionID=weightloss_circuit.ID),
        workoutRoutine(Name="Jump Rope", RepsDuration="30 secs, 20s rest", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=12, SectionID=weightloss_circuit.ID),
        workoutRoutine(Name="Plank with Shoulder Taps", RepsDuration="30 secs, 20s rest", RoutineDescription="Hold plank, tap opposite shoulder, alternate sides", ExerciseOrder=13, SectionID=weightloss_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stand tall, fold forward, stretch hamstrings completely", ExerciseOrder=14, SectionID=weightloss_cooldown.ID),
        workoutRoutine(Name="Chest & Shoulder Stretch", RepsDuration="30 seconds", RoutineDescription="Clasp hands behind back and gently lift", ExerciseOrder=15, SectionID=weightloss_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=weightloss_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Hold one foot behind to stretch the front of the thigh", ExerciseOrder=17, SectionID=weightloss_cooldown.ID),
        workoutRoutine(Name="Deep Breathing", RepsDuration="3-5 deep breaths", RoutineDescription="Inhale deeply, exhale slowly, and relax", ExerciseOrder=18, SectionID=weightloss_cooldown.ID),
    ]

    session.add_all(weightloss_section)
    
    endurance_warmup = session.query(workout_sections).filter_by(SectionName="Endurance Warm Up").first()
    endurance_circuit = session.query(workout_sections).filter_by(SectionName="Endurance Circuit").first()
    endurance_cooldown = session.query(workout_sections).filter_by(SectionName="Endurance Cool Down").first()

    endurance_section = [
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=endurance_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=endurance_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="15 reps", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=3, SectionID=endurance_warmup.ID),
        workoutRoutine(Name="Hip Openers", RepsDuration="30 seconds", RoutineDescription="Gently open hips, improve mobility, relax muscles", ExerciseOrder=4, SectionID=endurance_warmup.ID),
        workoutRoutine(Name="Inchworms to Push-Up", RepsDuration="5 reps", RoutineDescription="Walk hands forward, do push-up, return standing", ExerciseOrder=5, SectionID=endurance_warmup.ID),

        #Circuit
        workoutRoutine(Name="Jump Squats", RepsDuration="40 secs, 20s rest", RoutineDescription="Squat down, explode up, land softly, repeat", ExerciseOrder=6, SectionID=endurance_circuit.ID),
        workoutRoutine(Name="Push-Ups to Shoulder Tap", RepsDuration="40 secs, 20s rest", RoutineDescription="Push-up, then tap opposite shoulder", ExerciseOrder=7, SectionID=endurance_circuit.ID),
        workoutRoutine(Name="Burpees", RepsDuration="40 secs, 20s rest", RoutineDescription="Squat, jump back, push-up, jump up explosively", ExerciseOrder=8, SectionID=endurance_circuit.ID),
        workoutRoutine(Name="Kettlebell Swings", RepsDuration="40 secs, 20s rest", RoutineDescription="Hinge hips, swing kettlebell up, control down", ExerciseOrder=9, SectionID=endurance_circuit.ID),
        workoutRoutine(Name="Mountain Climbers", RepsDuration="40 secs, 20s rest", RoutineDescription="Run knees toward chest in a plank position", ExerciseOrder=10, SectionID=endurance_circuit.ID),
        workoutRoutine(Name="Lunges with Dumbbells", RepsDuration="40 secs, 20s rest", RoutineDescription="Or Bodyweight. Walking or Stationary each side. Step forward, lower knee, hold dumbbells steadily", ExerciseOrder=11, SectionID=endurance_circuit.ID),
        workoutRoutine(Name="Plank to Knee Tucks", RepsDuration="40 secs, 20s rest", RoutineDescription="Bring knees to chest in a plank", ExerciseOrder=12, SectionID=endurance_circuit.ID),
        workoutRoutine(Name="Jump Rope", RepsDuration="40 secs, 20s rest", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=13, SectionID=endurance_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Stand tall, extend leg, reach toward toes", ExerciseOrder=14, SectionID=endurance_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=15, SectionID=endurance_cooldown.ID),
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=16, SectionID=endurance_cooldown.ID),
        workoutRoutine(Name="Downward Dog to Cobra Stretch", RepsDuration="30 seconds", RoutineDescription="Shift from hips up to chest lifted position", ExerciseOrder=17, SectionID=endurance_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=18, SectionID=endurance_cooldown.ID),
    ]

    session.add_all(endurance_section)
    
    mobility_warmup = session.query(workout_sections).filter_by(SectionName="Flexibility and Mobility Warm Up").first()
    mobility_circuit = session.query(workout_sections).filter_by(SectionName="Flexibility and Mobility Circuit").first()
    mobility_cooldown = session.query(workout_sections).filter_by(SectionName="Flexibility and Mobility Cool Down").first()
    
    mobility_section = [
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=mobility_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=mobility_warmup.ID),
        workoutRoutine(Name="Hip Circles & Leg Swings", RepsDuration="30 seconds", RoutineDescription="30 sec per side. Rotate hips, then swing legs front-to-back and side-to-side", ExerciseOrder=3, SectionID=mobility_warmup.ID),
        workoutRoutine(Name="Deep Bodyweight Squats with Hold", RepsDuration="30 seconds", RoutineDescription="Squat low, hold position, engage core, balance", ExerciseOrder=4, SectionID=mobility_warmup.ID),
        workoutRoutine(Name="Worlds Greatest Stretch", RepsDuration="30 seconds", RoutineDescription="Lunge forward, rotate torso, reach arm upward 30 seconds each side", ExerciseOrder=5, SectionID=mobility_warmup.ID),

        #Circuit
        workoutRoutine(Name="Cossack Squats", RepsDuration="40 secs, 20s rest", RoutineDescription="Deep lateral squats targeting hips and legs", ExerciseOrder=6, SectionID=mobility_circuit.ID),
        workoutRoutine(Name="Single-Leg Romanian Deadlifts", RepsDuration="40 secs, 20s rest", RoutineDescription="Hinge forward on one leg, lower weight, return up", ExerciseOrder=7, SectionID=mobility_circuit.ID),
        workoutRoutine(Name="Bear Crawls", RepsDuration="40 secs, 20s rest", RoutineDescription="Crawl forward on hands and feet, keep low", ExerciseOrder=8, SectionID=mobility_circuit.ID),
        workoutRoutine(Name="Spiderman Lunges with Reach", RepsDuration="40 secs, 20s rest", RoutineDescription="Lunge forward, drop hips, extend arm upward", ExerciseOrder=9, SectionID=mobility_circuit.ID),
        workoutRoutine(Name="Controlled Jump Squats", RepsDuration="40 secs, 20s rest", RoutineDescription="Squat down, explode up, land softly, repeat", ExerciseOrder=10, SectionID=mobility_circuit.ID),
        workoutRoutine(Name="Slow Eccentric Push-Ups", RepsDuration="40 secs, 20s rest", RoutineDescription="Lower chest slowly, control movement, push up normally", ExerciseOrder=11, SectionID=mobility_circuit.ID),
        workoutRoutine(Name="Resistance Band Shoulder Dislocates", RepsDuration="40 secs, 20s rest", RoutineDescription="Hold band, lift overhead, rotate shoulders back", ExerciseOrder=12, SectionID=mobility_circuit.ID),
        workoutRoutine(Name="Skaters", RepsDuration="40 secs, 20s rest", RoutineDescription="Side-to-Side Bounds", ExerciseOrder=13, SectionID=mobility_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=14, SectionID=mobility_cooldown.ID),
        workoutRoutine(Name="Pigeon Pose", RepsDuration="30 seconds", RoutineDescription="30 sec per side. Extend one leg back, fold front leg forward", ExerciseOrder=15, SectionID=mobility_cooldown.ID),
        workoutRoutine(Name="Downward Dog to Cobra Flow", RepsDuration="30 seconds", RoutineDescription="Move from hips up to chest lifted smoothly", ExerciseOrder=16, SectionID=mobility_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="Stretch front thigh by pulling foot back", ExerciseOrder=17, SectionID=mobility_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=18, SectionID=mobility_cooldown.ID),
    ]

    session.add_all(mobility_section)
    
    everyday_warmup = session.query(workout_sections).filter_by(SectionName="Everyday Movement Warm Up").first()
    everyday_circuit = session.query(workout_sections).filter_by(SectionName="Everyday Movement Circuit").first()
    everyday_cooldown = session.query(workout_sections).filter_by(SectionName="Everyday Movement Cool Down").first()

    everyday_section = [
        # Warm-up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=everyday_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=everyday_warmup.ID),
        workoutRoutine(Name="Hip Circles & Leg Swings", RepsDuration="30 seconds", RoutineDescription="30 sec per side. Rotate hips, then swing legs front-to-back and side-to-side", ExerciseOrder=3, SectionID=everyday_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats with Reach", RepsDuration="15 reps", RoutineDescription="Squat down, extend arms overhead, stand up", ExerciseOrder=4, SectionID=everyday_warmup.ID),
        workoutRoutine(Name="Inchworm to Shoulder Tap", RepsDuration="5 reps", RoutineDescription="Walk hands out, tap shoulder, return standing", ExerciseOrder=5, SectionID=everyday_warmup.ID),

        # Circuit
        workoutRoutine(Name="Squat to Press", RepsDuration="40 secs, 20s rest", RoutineDescription="Squat down, stand up, press weights overhead", ExerciseOrder=6, SectionID=everyday_circuit.ID),
        workoutRoutine(Name="Step-Ups", RepsDuration="40 secs, 20s rest", RoutineDescription="Step onto platform, drive through heel, switch legs", ExerciseOrder=7, SectionID=everyday_circuit.ID),
        workoutRoutine(Name="Push-Ups", RepsDuration="40 secs, 20s rest", RoutineDescription="Lower chest to floor, push up, keep core engaged", ExerciseOrder=8, SectionID=everyday_circuit.ID),
        workoutRoutine(Name="Deadlifts", RepsDuration="40 secs, 20s rest", RoutineDescription="Hinge at hips, lift weight, stand tall, lower controlled", ExerciseOrder=9, SectionID=everyday_circuit.ID),
        workoutRoutine(Name="Farmers Walk", RepsDuration="40 secs, 20s rest", RoutineDescription="Carry heavy weights, walk upright, engage core", ExerciseOrder=10, SectionID=everyday_circuit.ID),
        workoutRoutine(Name="Lunges with Twist", RepsDuration="40 secs, 20s rest", RoutineDescription="Step forward, lower knee, rotate torso sideways", ExerciseOrder=11, SectionID=everyday_circuit.ID),
        workoutRoutine(Name="Bear Crawl", RepsDuration="40 secs, 20s rest", RoutineDescription="Crawl forward on hands and feet, keep low", ExerciseOrder=12, SectionID=everyday_circuit.ID),
        workoutRoutine(Name="Jumping Jacks", RepsDuration="40 secs, 20s rest", RoutineDescription="Jump, spread legs, raise arms, return repeatedly", ExerciseOrder=13, SectionID=everyday_circuit.ID),

        # Cooldown
        workoutRoutine(Name="Standing Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Stand tall, extend leg, reach toward toes", ExerciseOrder=14, SectionID=everyday_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=15, SectionID=everyday_cooldown.ID),
        workoutRoutine(Name="Seated Figure Four Stretch", RepsDuration="30 seconds", RoutineDescription="Cross ankle over knee, lean forward, stretch hips", ExerciseOrder=16, SectionID=everyday_cooldown.ID),
        workoutRoutine(Name="Downward Dog to Cobra Flow", RepsDuration="30 seconds", RoutineDescription="Move from hips up to chest lifted smoothly", ExerciseOrder=17, SectionID=everyday_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=18, SectionID=everyday_cooldown.ID),
    ]

    session.add_all(everyday_section)
    
    fallrisk_warmup = session.query(workout_sections).filter_by(SectionName="Reducing Fall Warm Up").first()
    fallrisk_circuit = session.query(workout_sections).filter_by(SectionName="Reducing Fall Circuit").first()
    fallrisk_cooldown = session.query(workout_sections).filter_by(SectionName="Reducing Fall Cool Down").first()

    fallrisk_section = [
        #Warm up
        workoutRoutine(Name="Standing Marching in Place", RepsDuration="1 min", RoutineDescription="Lift knees alternately, engage core, maintain rhythm", ExerciseOrder=1, SectionID=fallrisk_warmup.ID),
        workoutRoutine(Name="Ankle Circles & Toe Taps", RepsDuration="30 seconds", RoutineDescription="Rotate ankles, tap toes, improve mobility, balance", ExerciseOrder=2, SectionID=fallrisk_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=3, SectionID=fallrisk_warmup.ID),
        workoutRoutine(Name="Heel-to-Toe Walk", RepsDuration="30 seconds", RoutineDescription="Step heel to toe, maintain balance, walk steadily", ExerciseOrder=4, SectionID=fallrisk_warmup.ID),
        workoutRoutine(Name="Gentle Bodyweight Squats", RepsDuration="12 reps", RoutineDescription="Slow, controlled squats with minimal impact", ExerciseOrder=5, SectionID=fallrisk_warmup.ID),

        #Circuit
        workoutRoutine(Name="Sit-to-Stand from a Chair", RepsDuration="40 secs, 20s rest", RoutineDescription="Rise from chair, engage legs, lower back down.", ExerciseOrder=6, SectionID=fallrisk_circuit.ID),
        workoutRoutine(Name="Heel Raises", RepsDuration="40 secs, 20s rest", RoutineDescription="Lift heels, balance on toes, lower down.", ExerciseOrder=7, SectionID=fallrisk_circuit.ID),
        workoutRoutine(Name="Single-Leg Balance", RepsDuration="40 secs, 20s rest", RoutineDescription="Stand on one leg, engage core, hold steady.", ExerciseOrder=8, SectionID=fallrisk_circuit.ID),
        workoutRoutine(Name="Side Leg Raises", RepsDuration="40 secs, 20s rest", RoutineDescription="Lift leg sideways, engage core, lower slowly.", ExerciseOrder=9, SectionID=fallrisk_circuit.ID),
        workoutRoutine(Name="Step-Ups", RepsDuration="40 secs, 20s rest", RoutineDescription="Step onto platform, drive through heel, switch legs.", ExerciseOrder=10, SectionID=fallrisk_circuit.ID),
        workoutRoutine(Name="Standing Shoulder Press", RepsDuration="40 secs, 20s rest", RoutineDescription="Press weights overhead, keep core engaged, lower controlled.", ExerciseOrder=11, SectionID=fallrisk_circuit.ID),
        workoutRoutine(Name="Gentle Lateral Side Steps", RepsDuration="40 secs, 20s rest", RoutineDescription="Step sideways slowly, maintain balance, engage legs.", ExerciseOrder=12, SectionID=fallrisk_circuit.ID),
        workoutRoutine(Name="Marching in Place with High Knees", RepsDuration="40 secs, 20s rest", RoutineDescription="Stand, march in place, lift knees high.", ExerciseOrder=13, SectionID=fallrisk_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Stand tall, extend leg, reach toward toes.", ExerciseOrder=14, SectionID=fallrisk_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=15, SectionID=fallrisk_cooldown.ID),
        workoutRoutine(Name="Seated Ankle Rolls & Foot Flexes", RepsDuration="30 seconds", RoutineDescription="Rotate ankles, flex feet, improve mobility gently.", ExerciseOrder=16, SectionID=fallrisk_cooldown.ID),
        workoutRoutine(Name="Gentle Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=17, SectionID=fallrisk_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Seated Position", RepsDuration="30 seconds", RoutineDescription="Inhale deeply, exhale slowly, relax body completely.", ExerciseOrder=18, SectionID=fallrisk_cooldown.ID),
    ]

    session.add_all(fallrisk_section)
    
    power_warmup = session.query(workout_sections).filter_by(SectionName="Power Training Warm Up").first()
    power_circuit = session.query(workout_sections).filter_by(SectionName="Power Training Circuit").first()
    power_cooldown = session.query(workout_sections).filter_by(SectionName="Power Training Cool Down").first()

    power_section = [
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=power_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=power_warmup.ID),
        workoutRoutine(Name="Leg Swings", RepsDuration="30 seconds", RoutineDescription="30 sec per side. Swing legs front-to-back and side-to-side", ExerciseOrder=3, SectionID=power_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats to Jump", RepsDuration="10 reps", RoutineDescription="Squat down, explode up, land softly", ExerciseOrder=4, SectionID=power_warmup.ID),
        workoutRoutine(Name="Inchworms to Push-Up", RepsDuration="5 reps", RoutineDescription="Walk hands forward, do push-up, return standing", ExerciseOrder=5, SectionID=power_warmup.ID),

        #Circuit
        workoutRoutine(Name="Jump Squats", RepsDuration="40 secs, 20s rest", RoutineDescription="Squat down, explode up, land softly, repeat", ExerciseOrder=6, SectionID=power_circuit.ID),
        workoutRoutine(Name="Dumbbell Snatch", RepsDuration="40 secs, 20s rest", RoutineDescription="Explosively lift dumbbell overhead, engage core, control descent", ExerciseOrder=7, SectionID=power_circuit.ID),
        workoutRoutine(Name="Box Jumps", RepsDuration="40 secs, 20s rest", RoutineDescription="Jump onto box, land softly, stand tall", ExerciseOrder=8, SectionID=power_circuit.ID),
        workoutRoutine(Name="Kettlebell Swings", RepsDuration="40 secs, 20s rest", RoutineDescription="Hinge hips, swing kettlebell up, control down", ExerciseOrder=9, SectionID=power_circuit.ID),
        workoutRoutine(Name="Medicine Ball Slams", RepsDuration="40 secs, 20s rest", RoutineDescription="Lift medicine ball overhead, slam it down forcefully", ExerciseOrder=10, SectionID=power_circuit.ID),
        workoutRoutine(Name="Broad Jumps", RepsDuration="40 secs, 20s rest", RoutineDescription="Jump forward explosively, land softly, repeat continuously", ExerciseOrder=11, SectionID=power_circuit.ID),
        workoutRoutine(Name="Push Press", RepsDuration="40 secs, 20s rest", RoutineDescription="Dip slightly, press weights overhead, extend arms fully", ExerciseOrder=12, SectionID=power_circuit.ID),
        workoutRoutine(Name="Sled Push", RepsDuration="40 secs, 20s rest", RoutineDescription="Drive sled forward, engage legs, maintain low posture", ExerciseOrder=13, SectionID=power_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="30 sec per leg. Stretch front thigh by pulling foot back", ExerciseOrder=14, SectionID=power_cooldown.ID),
        workoutRoutine(Name="Seated Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Sit, extend legs, reach toward toes, hold stretch. 30 seconds per leg", ExerciseOrder=15, SectionID=power_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=16, SectionID=power_cooldown.ID),
        workoutRoutine(Name="Downward Dog to Cobra Flow", RepsDuration="30 seconds", RoutineDescription="Move from hips up to chest lifted smoothly", ExerciseOrder=17, SectionID=power_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=18, SectionID=power_cooldown.ID),
    ]

    session.add_all(power_section)
    
    hiit_warmup = session.query(workout_sections).filter_by(SectionName="HIIT Warm Up").first()
    hiit_circuit = session.query(workout_sections).filter_by(SectionName="HIIT Circuit").first()
    hiit_cooldown = session.query(workout_sections).filter_by(SectionName="HIIT Cool Down").first()

    hiit_section = [
        #Warm up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=hiit_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=hiit_warmup.ID),
        workoutRoutine(Name="Leg Swings", RepsDuration="30 seconds", RoutineDescription="30 sec per leg. Swing legs front-to-back and side-to-side", ExerciseOrder=3, SectionID=hiit_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="15 reps", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=4, SectionID=hiit_warmup.ID),
        workoutRoutine(Name="Inchworms to Push-Up", RepsDuration="5 reps", RoutineDescription="Walk hands forward, do push-up, return standing", ExerciseOrder=5, SectionID=hiit_warmup.ID),

        #Circuit
        workoutRoutine(Name="Jump Squats", RepsDuration="40 secs, 20s rest", RoutineDescription="Squat down, explode up, land softly, repeat", ExerciseOrder=6, SectionID=hiit_circuit.ID),
        workoutRoutine(Name="Push-Ups to Shoulder Tap", RepsDuration="40 secs, 20s rest", RoutineDescription="Perform push-up, tap opposite shoulder, alternate sides", ExerciseOrder=7, SectionID=hiit_circuit.ID),
        workoutRoutine(Name="Burpees", RepsDuration="40 secs, 20s rest", RoutineDescription="Squat, jump back, push-up, jump up explosively", ExerciseOrder=8, SectionID=hiit_circuit.ID),
        workoutRoutine(Name="Kettlebell Swings", RepsDuration="40 secs, 20s rest", RoutineDescription="Hinge hips, swing kettlebell up, control down", ExerciseOrder=9, SectionID=hiit_circuit.ID),
        workoutRoutine(Name="Mountain Climbers", RepsDuration="40 secs, 20s rest", RoutineDescription="Run knees toward chest in a plank position", ExerciseOrder=10, SectionID=hiit_circuit.ID),
        workoutRoutine(Name="Lunges with Dumbbells", RepsDuration="40 secs, 20s rest", RoutineDescription="Or Bodyweight. Walking or Stationary each side. Step forward, lower knee, hold dumbbells steadily", ExerciseOrder=11, SectionID=hiit_circuit.ID),
        workoutRoutine(Name="Plank to Knee Tucks", RepsDuration="40 secs, 20s rest", RoutineDescription="Hold plank, drive knees toward chest, alternate sides", ExerciseOrder=12, SectionID=hiit_circuit.ID),
        workoutRoutine(Name="Jump Rope", RepsDuration="40 secs, 20s rest", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=13, SectionID=hiit_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Stand tall, extend leg, reach toward toes", ExerciseOrder=14, SectionID=hiit_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=15, SectionID=hiit_cooldown.ID),
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=16, SectionID=hiit_cooldown.ID),
        workoutRoutine(Name="Downward Dog to Cobra Flow", RepsDuration="30 seconds", RoutineDescription="Move from hips up to chest lifted smoothly", ExerciseOrder=17, SectionID=hiit_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=18, SectionID=hiit_cooldown.ID),
    ]

    session.add_all(hiit_section)
    
    mindbody_warmup = session.query(workout_sections).filter_by(SectionName="Mind and Body Warm Up").first()
    mindbody_circuit = session.query(workout_sections).filter_by(SectionName="Mind and Body Circuit").first()
    mindbody_cooldown = session.query(workout_sections).filter_by(SectionName="Mind and Body Cool Down").first()
    
    mindbody_section = [
        #Warm Up
        workoutRoutine(Name="Deep Breathing & Seated Neck Rolls", RepsDuration="30 seconds", RoutineDescription="Relax and center the mind", ExerciseOrder=1, SectionID=mindbody_warmup.ID),
        workoutRoutine(Name="Cat-Cow Stretch", RepsDuration="30 seconds", RoutineDescription="Arch and round back, flow between positions smoothly", ExerciseOrder=2, SectionID=mindbody_warmup.ID),
        workoutRoutine(Name="Standing Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=3, SectionID=mindbody_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats with Breath Control", RepsDuration="10 reps", RoutineDescription="Inhale down, exhale up. Lower hips, bend knees, stand up", ExerciseOrder=4, SectionID=mindbody_warmup.ID),
        workoutRoutine(Name="Downward Dog to Cobra Flow", RepsDuration="1 min", RoutineDescription="Move from hips up to chest lifted smoothly", ExerciseOrder=5, SectionID=mindbody_warmup.ID),

        #Circuit
        workoutRoutine(Name="Slow, Controlled Bodyweight Squats", RepsDuration="40 secs, 20s rest", RoutineDescription="Lower slowly, engage muscles, rise with control", ExerciseOrder=6, SectionID=mindbody_circuit.ID),
        workoutRoutine(Name="Plank to Downward Dog Flow", RepsDuration="40 secs, 20s rest", RoutineDescription="Shift from plank to downward dog, repeat smoothly", ExerciseOrder=7, SectionID=mindbody_circuit.ID),
        workoutRoutine(Name="Single-Leg Balance Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Stand on one leg, engage core, hold steady", ExerciseOrder=8, SectionID=mindbody_circuit.ID),
        workoutRoutine(Name="Resistance Band Row", RepsDuration="40 secs, 20s rest", RoutineDescription="Pull band towards chest, squeeze shoulder blades together", ExerciseOrder=9, SectionID=mindbody_circuit.ID),
        workoutRoutine(Name="Standing Tai Chi Arm Circles", RepsDuration="40 secs, 20s rest", RoutineDescription="Move arms in slow, controlled circular motions", ExerciseOrder=10, SectionID=mindbody_circuit.ID),
        workoutRoutine(Name="Side-Lying Leg Lifts", RepsDuration="40 secs, 20s rest", RoutineDescription="Lie on side, lift leg, lower slowly", ExerciseOrder=11, SectionID=mindbody_circuit.ID),
        workoutRoutine(Name="Standing Forward Fold to Halfway Lift", RepsDuration="40 secs, 20s rest", RoutineDescription="Fold forward, then halfway lift, elongate spine", ExerciseOrder=12, SectionID=mindbody_circuit.ID),
        workoutRoutine(Name="Controlled High Knee Marching", RepsDuration="40 secs, 20s rest", RoutineDescription="Do it with Deep Breathing", ExerciseOrder=13, SectionID=mindbody_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=14, SectionID=mindbody_cooldown.ID),
        workoutRoutine(Name="Childs Pose with Deep Breathing", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=15, SectionID=mindbody_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=16, SectionID=mindbody_cooldown.ID),
        workoutRoutine(Name="Reclined Butterfly Pose", RepsDuration="30 seconds", RoutineDescription="Lie back, soles together, relax hips outward gently", ExerciseOrder=17, SectionID=mindbody_cooldown.ID),
        workoutRoutine(Name="Savasana", RepsDuration="1 min", RoutineDescription="Lie flat, relax completely, focus on breathing", ExerciseOrder=18, SectionID=mindbody_cooldown.ID),
    ]

    session.add_all(mindbody_section)
    
    agility_warmup = session.query(workout_sections).filter_by(SectionName="Agility Warm Up").first()
    agility_circuit = session.query(workout_sections).filter_by(SectionName="Agility Circuit").first()
    agility_cooldown = session.query(workout_sections).filter_by(SectionName="Agility Cool Down").first()

    agility_section = [
        #Warm Up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=agility_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=agility_warmup.ID),
        workoutRoutine(Name="Leg Swings", RepsDuration="30 seconds", RoutineDescription="30 sec per leg, swing legs front-to-back and side-to-side", ExerciseOrder=3, SectionID=agility_warmup.ID),
        workoutRoutine(Name="High Knees", RepsDuration="30 seconds", RoutineDescription="Lift knees rapidly while running in place", ExerciseOrder=4, SectionID=agility_warmup.ID),
        workoutRoutine(Name="Lateral Lunges", RepsDuration="10 reps", RoutineDescription="10 reps per side. Step sideways, bend one knee, keep balance", ExerciseOrder=5, SectionID=agility_warmup.ID),

        #Circuit
        workoutRoutine(Name="Agility Ladder Drills", RepsDuration="40 secs, 20s rest", RoutineDescription="Quick footwork through ladder, improve speed, coordination", ExerciseOrder=6, SectionID=agility_circuit.ID),
        workoutRoutine(Name="Lateral Cone Shuffles", RepsDuration="40 secs, 20s rest", RoutineDescription="Shuffle sideways quickly, stay low, move around cones", ExerciseOrder=7, SectionID=agility_circuit.ID),
        workoutRoutine(Name="Hurdle Jumps", RepsDuration="40 secs, 20s rest", RoutineDescription="Jump over hurdles, land softly, maintain controlled movement", ExerciseOrder=8, SectionID=agility_circuit.ID),
        workoutRoutine(Name="Reaction Sprint", RepsDuration="40 secs, 20s rest", RoutineDescription="Sprint 5-10 Yards, Jog Back, Repeat", ExerciseOrder=9, SectionID=agility_circuit.ID),
        workoutRoutine(Name="Skaters", RepsDuration="40 secs, 20s rest", RoutineDescription="Side-to-Side Bounds", ExerciseOrder=10, SectionID=agility_circuit.ID),
        workoutRoutine(Name="Burpees with a Lateral Jump", RepsDuration="40 secs, 20s rest", RoutineDescription="Perform burpee, jump sideways, repeat movement continuously", ExerciseOrder=11, SectionID=agility_circuit.ID),
        workoutRoutine(Name="Forward-Backward Sprints", RepsDuration="40 secs, 20s rest", RoutineDescription="5 Yards Each Way", ExerciseOrder=12, SectionID=agility_circuit.ID),
        workoutRoutine(Name="Medicine Ball Slams", RepsDuration="40 secs, 20s rest", RoutineDescription="Lift medicine ball overhead, slam it down forcefully", ExerciseOrder=13, SectionID=agility_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Stand tall, extend leg, reach toward toes", ExerciseOrder=14, SectionID=agility_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=15, SectionID=agility_cooldown.ID),
        workoutRoutine(Name="Quadriceps Stretch", RepsDuration="30 seconds", RoutineDescription="Stand tall, pull foot back, stretch front thigh", ExerciseOrder=16, SectionID=agility_cooldown.ID),
        workoutRoutine(Name="Downward Dog to Cobra Stretch", RepsDuration="30 seconds", RoutineDescription="Shift from hips up to chest lifted position", ExerciseOrder=17, SectionID=agility_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=18, SectionID=agility_cooldown.ID),
    ]

    session.add_all(agility_section)
    
    isometric_warmup = session.query(workout_sections).filter_by(SectionName="Isometric Training Warm Up").first()
    isometric_circuit = session.query(workout_sections).filter_by(SectionName="Isometric Training Circuit").first()
    isometric_cooldown = session.query(workout_sections).filter_by(SectionName="Isometric Training Cool Down").first()

    isometric_section = [
        
        #Warm Up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=isometric_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=isometric_warmup.ID),
        workoutRoutine(Name="Deep Bodyweight Squat Hold", RepsDuration="10 seconds", RoutineDescription="10 Sec, 3 Rounds", ExerciseOrder=3, SectionID=isometric_warmup.ID),
        workoutRoutine(Name="Plank to Downward Dog Flow", RepsDuration="30 seconds", RoutineDescription="Shift from plank to downward dog, repeat smoothly", ExerciseOrder=4, SectionID=isometric_warmup.ID),
        workoutRoutine(Name="Hip Bridges", RepsDuration="10 reps", RoutineDescription="Lift hips, squeeze glutes, lower back down", ExerciseOrder=5, SectionID=isometric_warmup.ID),

        #Circuit
        workoutRoutine(Name="Wall Sit", RepsDuration="40 secs, 20s rest", RoutineDescription="Press back against wall, bend knees, hold position", ExerciseOrder=6, SectionID=isometric_circuit.ID),
        workoutRoutine(Name="Plank Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Keep body straight, engage core, hold position", ExerciseOrder=7, SectionID=isometric_circuit.ID),
        workoutRoutine(Name="Isometric Lunge Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Hold lunge position, engage legs, maintain stability", ExerciseOrder=8, SectionID=isometric_circuit.ID),
        workoutRoutine(Name="Push-Up Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Lower halfway, hold position, engage core and arms", ExerciseOrder=9, SectionID=isometric_circuit.ID),
        workoutRoutine(Name="Superman Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Lie face down, lift arms and legs, hold position", ExerciseOrder=10, SectionID=isometric_circuit.ID),
        workoutRoutine(Name="Isometric Biceps Curl", RepsDuration="40 secs, 20s rest", RoutineDescription="Hold dumbbells at 90-degree bend, engage biceps", ExerciseOrder=11, SectionID=isometric_circuit.ID),
        workoutRoutine(Name="Glute Bridge Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Hips up, squeeze glutes", ExerciseOrder=12, SectionID=isometric_circuit.ID),
        workoutRoutine(Name="Side Plank Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Balance on one side, engage core, hold position", ExerciseOrder=13, SectionID=isometric_circuit.ID),

        #Cool down
        workoutRoutine(Name="Seated Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Sit, extend legs, reach toward toes, hold stretch. 30 seconds per leg", ExerciseOrder=14, SectionID=isometric_cooldown.ID),
        workoutRoutine(Name="Standing Quad Stretch", RepsDuration="30 seconds", RoutineDescription="30 sec per leg. Stretch front thigh by pulling foot back", ExerciseOrder=15, SectionID=isometric_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=16, SectionID=isometric_cooldown.ID),
        workoutRoutine(Name="Childs Pose with Deep Breathing", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=17, SectionID=isometric_cooldown.ID),
        workoutRoutine(Name="Seated Spinal Twist", RepsDuration="30 seconds", RoutineDescription="Sit, cross one leg over, twist torso gently", ExerciseOrder=18, SectionID=isometric_cooldown.ID),
    ]

    session.add_all(isometric_section)
    
    strength_warmup = session.query(workout_sections).filter_by(SectionName="Strength Training Warm Up").first()
    strength_circuit = session.query(workout_sections).filter_by(SectionName="Strength Training Circuit").first()
    strength_cooldown = session.query(workout_sections).filter_by(SectionName="Strength Training Cool Down").first()

    strength_section = [
        #Warm Up
        workoutRoutine(Name="Jump Rope", RepsDuration="1 min", RoutineDescription="Jump continuously over a swinging rope", ExerciseOrder=1, SectionID=strength_warmup.ID),
        workoutRoutine(Name="Arm Circles & Shoulder Rolls", RepsDuration="30 seconds", RoutineDescription="30 sec each direction. Rotate arms, then roll shoulders forward and back", ExerciseOrder=2, SectionID=strength_warmup.ID),
        workoutRoutine(Name="Bodyweight Squats", RepsDuration="15 reps", RoutineDescription="Lower hips, bend knees, stand up", ExerciseOrder=3, SectionID=strength_warmup.ID),
        workoutRoutine(Name="Hip Bridges", RepsDuration="10 reps", RoutineDescription="Lift hips, squeeze glutes, lower back down", ExerciseOrder=4, SectionID=strength_warmup.ID),
        workoutRoutine(Name="Inchworms to Push-Up", RepsDuration="5 reps", RoutineDescription="Walk hands forward, do push-up, return standing", ExerciseOrder=5, SectionID=strength_warmup.ID),

        #Circuit
        workoutRoutine(Name="Squats", RepsDuration="40 secs, 20s rest", RoutineDescription="Lower hips, bend knees, then stand up", ExerciseOrder=6, SectionID=strength_circuit.ID),
        workoutRoutine(Name="Deadlifts", RepsDuration="40 secs, 20s rest", RoutineDescription="Hinge at hips, lift weight, stand tall, lower controlled", ExerciseOrder=7, SectionID=strength_circuit.ID),
        workoutRoutine(Name="Push-Ups", RepsDuration="40 secs, 20s rest", RoutineDescription="Lower chest to floor, push up, keep core engaged", ExerciseOrder=8, SectionID=strength_circuit.ID),
        workoutRoutine(Name="Bent-Over Rows", RepsDuration="40 secs, 20s rest", RoutineDescription="Hinge forward, pull weights to torso, lower slowly", ExerciseOrder=9, SectionID=strength_circuit.ID),
        workoutRoutine(Name="Lunges", RepsDuration="40 secs, 20s rest", RoutineDescription="Bodyweight or Weighted. Alternate legs. Step forward, lower knee, push back up", ExerciseOrder=10, SectionID=strength_circuit.ID),
        workoutRoutine(Name="Overhead Shoulder Press", RepsDuration="40 secs, 20s rest", RoutineDescription="Press weights overhead, extend arms fully, lower controlled", ExerciseOrder=11, SectionID=strength_circuit.ID),
        workoutRoutine(Name="Plank Hold", RepsDuration="40 secs, 20s rest", RoutineDescription="Keep body straight, engage core, hold position", ExerciseOrder=12, SectionID=strength_circuit.ID),
        workoutRoutine(Name="Russian Twists", RepsDuration="40 secs, 20s rest", RoutineDescription="Bodyweight or Dumbbell. Sit, twist torso side to side, engage core", ExerciseOrder=13, SectionID=strength_circuit.ID),

        #Cool down
        workoutRoutine(Name="Standing Hamstring Stretch", RepsDuration="30 seconds", RoutineDescription="Stand tall, extend leg, reach toward toes", ExerciseOrder=14, SectionID=strength_cooldown.ID),
        workoutRoutine(Name="Chest Opener Stretch", RepsDuration="30 seconds", RoutineDescription="Expand chest by pulling arms back", ExerciseOrder=15, SectionID=strength_cooldown.ID),
        workoutRoutine(Name="Seated Forward Fold", RepsDuration="30 seconds", RoutineDescription="Stretch hamstrings by reaching toward toes", ExerciseOrder=16, SectionID=strength_cooldown.ID),
        workoutRoutine(Name="Downward Dog to Cobra Stretch", RepsDuration="30 seconds", RoutineDescription="Shift from hips up to chest lifted", ExerciseOrder=17, SectionID=strength_cooldown.ID),
        workoutRoutine(Name="Deep Breathing in Childs Pose", RepsDuration="30 seconds", RoutineDescription="Hold the stretch for 30-40 seconds. Kneel, stretch arms forward, relax back", ExerciseOrder=18, SectionID=strength_cooldown.ID),
    ]

    session.add_all(strength_section)"""