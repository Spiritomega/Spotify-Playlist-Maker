# **Spotify Playlist Time Travel Script**

This Python script takes you on a musical journey through time by creating a Spotify playlist based on Billboard's Top 100 songs from a specific date. It's perfect for reliving the music of your favorite year or discovering the hits from a significant moment in history.

---

### **Features**
1. **Fetch Top 100 Songs**: Retrieves the Billboard Top 100 songs for a user-specified date using web scraping.
2. **Spotify Playlist Creation**: Searches for the songs on Spotify and creates a private playlist automatically.
3. **Batch Song Lookup**: Handles multiple songs, ensuring seamless playlist creation.
4. **Customizable Time Travel**: Users can input any date (in `YYYY-MM-DD` format) to explore the music of that era.

---

### **How It Works**
1. **Input a Date**: Provide a specific date (e.g., `2000-08-12`) when prompted.
2. **Retrieve Songs**: The script scrapes the Billboard website to fetch the Top 100 songs for the given date.
3. **Search on Spotify**: It searches for each song on Spotify using their API.
4. **Create Playlist**: The script creates a private Spotify playlist containing the songs found for that year.

---

### **Requirements**
- **Python Libraries**: 
  - `requests`
  - `BeautifulSoup` (from `bs4`)
  - `spotipy`
- **Spotify Developer Credentials**: 
  - A Spotify Developer account to get your **Client ID**, **Client Secret**, and **Redirect URL**.
- **Billboard URL Access**: Ensure the Billboard charts page for the desired date is accessible.

---

### **Setup Instructions**
1. Clone the repository and navigate to the script's directory.
2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 spotipy
   ```
3. Set up your Spotify Developer account and create an app to obtain:
   - **Client ID**
   - **Client Secret**
   - **Redirect URL**
4. Replace the following placeholders in the script:
   - `CLIENT_ID` with your Spotify Client ID.
   - `CLIENT_SECRET` with your Spotify Client Secret.
   - `REDIRECT_URL` with your app's redirect URL.
   - `username` with your Spotify username.
5. Run the script:
   ```bash
   python script_name.py
   ```
6. Enter the desired date when prompted and enjoy your Spotify playlist!

---

### **Limitations**
- Not all Billboard songs may be available on Spotify.
- Requires a stable internet connection for both scraping and API calls.

---

### **Use Cases**
- Relive your favorite year's hits.
- Create themed playlists for nostalgic events or parties.
- Discover and explore music from different decades.

---

### **Future Improvements**
- Add error handling for missing songs.
- Make playlists public or shareable on-demand.
- Support other music charts besides Billboard. 

---

Enjoy your personalized musical time travel experience! 🚀🎶
