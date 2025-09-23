# plan how many songs to listen to

def calculate_number_of_songs(hours: float, avg_song_length: float = 3.5) -> int:
    return int((hours * 60) // avg_song_length) #// ใช้เพื่อปัดลงเป็นจำนวนเต็มของเพลงที่ฟังได้จริง

print(calculate_number_of_songs(2,4))