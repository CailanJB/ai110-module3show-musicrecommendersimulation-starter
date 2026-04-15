"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded Songs: {len(songs)} ")

    # Distinct taste profiles used for content-based comparison
    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            # "mood": "happy",
            "energy": 0.90,
            "acousticness": 0.20,
            "danceability": 0.88,
        },
        "Chill Lofi": {
            "genre": "lofi",
            # "mood": "focused",
            "energy": 0.35,
            "acousticness": 0.85,
            "danceability": 0.55,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            # "mood": "intense",
            "energy": 0.95,
            "acousticness": 0.12,
            "danceability": 0.42,
        },
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nTop recommendations for {profile_name}:\n")
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song['title']}")
            print(f"   Score: {score:.2f}/10")
            print(f"   Why: {explanation}")
            print()

    # # Adversarial and edge-case profiles to test if scoring can be tricked.
    # adversarial_profiles = {
    #     "Contradictory: Sad But Explosive Pop": {
    #         "genre": "pop",
    #         "mood": "sad",
    #         "energy": 0.95,
    #         "acousticness": 0.10,
    #         "danceability": 0.90,
    #     },
    #     "Contradictory: Intense But Low-Energy Rock": {
    #         "genre": "rock",
    #         "mood": "intense",
    #         "energy": 0.05,
    #         "acousticness": 0.15,
    #         "danceability": 0.35,
    #     },
    #     "Danceability Sensitivity A (0.00)": {
    #         "genre": "pop",
    #         "mood": "happy",
    #         "energy": 0.70,
    #         "acousticness": 0.25,
    #         "danceability": 0.00,
    #     },
    #     "Danceability Sensitivity B (1.00)": {
    #         "genre": "pop",
    #         "mood": "happy",
    #         "energy": 0.70,
    #         "acousticness": 0.25,
    #         "danceability": 1.00,
    #     },
    #     "Out-of-Range Stress Test": {
    #         "genre": "electronic",
    #         "mood": "calm",
    #         "energy": 1.40,
    #         "acousticness": -0.30,
    #         "danceability": 1.50,
    #     },
    # }

    # for profile_name, user_prefs in adversarial_profiles.items():
    #     recommendations = recommend_songs(user_prefs, songs, k=5)

    #     print(f"\nAdversarial test recommendations for {profile_name}:\n")
    #     for i, rec in enumerate(recommendations, 1):
    #         song, score, explanation = rec
    #         print(f"{i}. {song['title']}")
    #         print(f"   Score: {score:.2f}/10")
    #         print(f"   Why: {explanation}")
    #         print()


if __name__ == "__main__":
    main()
