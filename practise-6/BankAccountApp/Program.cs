        // Create the first bank account
        BankAccount bankAccount1 = new BankAccount();
        bankAccount1.Name = "Nirjhor";
        bankAccount1.AccountNo = "2362738292";
        bankAccount1.Deposit(20000);
        bankAccount1.Withdraw(4000);

        // Create the second bank account
        BankAccount bankAccount2 = new BankAccount();
        bankAccount2.Name = "Mahadi";
        bankAccount2.AccountNo = "783238923";
        bankAccount2.Deposit(65000);

        // Add accounts to a list
        List<BankAccount> bankAccountList = new List<BankAccount>();
        bankAccountList.Add(bankAccount1);
        bankAccountList.Add(bankAccount2);

        // Calculate the total deposited amount
        double totalDepositedAmount = 0;
        foreach (BankAccount bankAccount in bankAccountList)
        {
            totalDepositedAmount += bankAccount.Balance; // Use a method to access Balance
        }

        // Output the total deposited amount
        Console.WriteLine($"Total deposited amount: {totalDepositedAmount}");