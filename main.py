from database import SessionLocal, Base, workouts, workout_sections, workoutRoutine

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
"""

       
with SessionLocal.begin() as session:
    workout1_warm_up = ()
    workout1_circuit = ()
    workout1_cool_down = ()



