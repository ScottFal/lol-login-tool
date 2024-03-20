from Utils.accountUtils import getAllAccounts
from Utils.tkinterUtils import createAccountWindow
from Utils.windowsUtils import callSubprocess, isWindowActive, isKeyPressed, enterAccountDetails

if __name__ == "__main__":
    enterKey = "enter"
    riotClientName = "Riot Client"
    leagueClientPath = r"C:\Riot Games\League of Legends\LeagueClient.exe"

    accounts = getAllAccounts()
    selectAccount = createAccountWindow(accounts)
    if selectAccount is not None:
        callSubprocess(leagueClientPath)
        while True:
            if isWindowActive(riotClientName) and isKeyPressed(enterKey):
                break

        enterAccountDetails(selectAccount.username, selectAccount.password)
