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

with SessionLocal.begin() as session:
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

    
"""with SessionLocal.begin() as session:
    session.query(workout_sections).filter(workout_sections.WOID==21).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==22).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==23).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==24).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==25).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==26).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==27).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==28).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==29).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==30).delete(synchronize_session=False)
"""
"""with SessionLocal.begin() as session:
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
"""

"""with SessionLocal.begin() as session:
    session.execute(text('ALTER SEQUENCE "Workout_Sections_ID_seq" RESTART WITH 1'))
    session.commit()"""
    
  
"""with SessionLocal.begin() as session:
    session.query(workout_sections).filter(workout_sections.WOID==1).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==2).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==3).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==4).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==5).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==6).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==7).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==8).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==9).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==10).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==11).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==12).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==13).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==14).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==15).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==16).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==17).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==18).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==19).delete(synchronize_session=False) 
    session.query(workout_sections).filter(workout_sections.WOID==20).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==21).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==22).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==23).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==24).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==25).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==26).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==27).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==28).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==29).delete(synchronize_session=False)
    session.query(workout_sections).filter(workout_sections.WOID==30).delete(synchronize_session=False)
    
session.commit()"""
    
    


