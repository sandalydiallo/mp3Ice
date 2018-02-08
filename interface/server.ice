module app
{
    struct music
    {
        string name;
        string genre;
        string author;
        string url;
    }

    sequence<music> tab;
    sequence<byte> file;

    interface Server
    {
        string addDocument(music music);
        string removeDocument(string name);
		tab  displayListMusic();
        tab  searchDocument(string attribute, string name);
        file downloadDocument(music music);
		void testLibvlcPlayer();
    }
}