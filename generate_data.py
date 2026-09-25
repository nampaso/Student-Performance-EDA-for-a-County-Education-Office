import os
import numpy as np
import pandas as pd


def generate_student_data(seed=55, n_samples=1200):
    np.random.seed(seed)

    counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Kiambu"]
    school_types = ["Public", "Private"]
    genders = ["Female", "Male"]

    student_ids = [f"STD{str(i).zfill(5)}" for i in range(1, n_samples + 1)]
    county_choice = np.random.choice(
        counties, size=n_samples, p=[0.3, 0.2, 0.2, 0.15, 0.15]
    )
    school_choice = np.random.choice(school_types, size=n_samples, p=[0.65, 0.35])
    gender_choice = np.random.choice(genders, size=n_samples)

    study_hours = np.random.normal(loc=15, scale=5, size=n_samples)
    study_hours = np.clip(study_hours, 1, 40)
    # Add a couple of realistic high outliers in study_hours
    study_hours[12] = 38.5
    study_hours[88] = 39.2

    attendance_pct = np.random.beta(a=5, b=1.5, size=n_samples) * 100
    attendance_pct = np.clip(attendance_pct, 40, 100)

    # Base score affected by study hours, attendance, and school type
    base_ability = (study_hours * 1.2) + (attendance_pct * 0.4)
    public_penalty = np.where(school_choice == "Public", -5, 3)

    math_score = base_ability + public_penalty + np.random.normal(0, 8, n_samples)
    english_score = base_ability + public_penalty + np.random.normal(0, 7, n_samples)
    science_score = base_ability + public_penalty + np.random.normal(0, 9, n_samples)

    # Clip scores to valid range [0, 100]
    math_score = np.clip(math_score, 15, 98)
    english_score = np.clip(english_score, 20, 99)
    science_score = np.clip(science_score, 10, 100)

    df = pd.DataFrame(
        {
            "student_id": student_ids,
            "county": county_choice,
            "school_type": school_choice,
            "gender": gender_choice,
            "study_hours": np.round(study_hours, 1),
            "attendance_pct": np.round(attendance_pct, 1),
            "math_score": np.round(math_score, 1),
            "english_score": np.round(english_score, 1),
            "science_score": np.round(science_score, 1),
        }
    )

    return df


if __name__ == "__main__":
    df = generate_student_data(seed=55)
    df.to_csv("student_performance.csv", index=False)
    print("student_performance.csv generated successfully!")
