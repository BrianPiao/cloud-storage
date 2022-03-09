import dropbox 
class transferdata:
    def __init__ (self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
         #link the our dropbox account to the application
          dbx = dropbox.Dropbox(self.access_token)
          f = open(file_from,'rb')
          #upload these contents to the dropbox using the files_upload() method
          dbx.files_upload(f.read(), file_to )


def main():
    access_token='sl.BDcFpqDwnGpP02WJSxjqI9EUZl5MmP1SaRSZ_Elsc__jObi2i98fOcPSZI0IIa3KFgZDS-GW7T0TnzyHxABbiQArBaP6MNTKKuk05OS3sVYaR09lHoYbzZL0ANOBBBXRDenJKskhcwD_'
    #creating object for class
    pd=transferdata (access_token)

    file_from = input("Enter the file path to transfer : ")
    file_2 = input("enter the  path to upload to dropbox : ")

    #function defined in the class "TransferData" is called
    pd.upload_file(file_from,file_2)
    print ("files moved")
main()