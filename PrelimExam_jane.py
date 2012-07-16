class Track:
    def SetInfo(self,name,artist,genre):
        self.Name=name
        self.Artist=artist
        self.Genre=genre
    def show(self):
        print("Name: %s " % (self.Name))
        print("Artist: %s " % (self.Artist))
        print("Genre: %s " % (self.Genre))

ListOfArtist=[]
artistInfo=Track()
artistInfo.SetInfo("Carly Rae Jepsen","Call Me Maybe","Pop Artist")
ListOfArtist.append(artistInfo)


class FavoriteMusic(Track):
    pass

class TopTen(Track):
    pass


for artist in ListOfArtist:
    artistInfo.show()

















