

class BankAccount {
    public string Name {set; get;}
    public string AccountNo {set; get;}
    public double Balance {private set; get;}

    public void Deposit(double amount){
        Balance = Balance + amount;
    }

    public void Withdraw(double amount){
        if (Balance - amount > 0){
            Balance = Balance - amount;
        }
        else {
            throw new ApplicationException("Insufficient balance!");
        }
    }
}