# plan how many songs to listen to

# def calculate_number_of_songs(hours: float, avg_song_length: float = 3.5) -> int:
#     return int((hours * 60) // avg_song_length) #// ใช้เพื่อปัดลงเป็นจำนวนเต็มของเพลงที่ฟังได้จริง

# print(calculate_number_of_songs(2,4))

def calculate_number_of_songs(hours: float, avg_song_length: float = 3.5) -> int:
    return (hours * 60) // avg_song_length

if __name__ == "__main__":
    hours, avg_song_length = 2, 4
    print(calculate_number_of_songs(hours, avg_song_length))