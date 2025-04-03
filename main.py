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
    
    session.add_all(sections)"""
    
with SessionLocal.begin() as session:
    """beginner_warmup = session.query(workout_sections).filter_by(SectionName="Beginner Warm Up").first()
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
    ]"""
    
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