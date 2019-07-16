def test(func, args, expected):
    """
    Basic testing suite.
    
        func -> a function
        args -> list of tuples
        expected -> list of expected return values
    
    Requires len(args) == len(expected)
    """
    
    # Header and initialization
    print("TESTING {}".format(func.__name__).center(30))
    print("="*30)
    num_failed, which_failed = 0, []
    
    for i, (arg, exp) in enumerate(zip(args, expected)):
        # Compute and print out results/comparisons for each test case
        computed = func(*arg)
        print("Test {}:  {}({:.25}...)".format(i, func.__name__, str(arg)))
        print("  Computed: {}".format(computed))
        print("  Expected: {}".format(exp))
        
        # note and count failures
        if func(*arg) != exp:
            print(computed, exp)
            print("TEST {} FAILED".format(i).center(30))
            which_failed.append(i)
            num_failed += 1   
        print("-"*30)
    print("="*30)
    
    # Summary
    print("The following {} {} failing:".format(num_failed, {0: 'test is', 1: 'tests are'}[num_failed != 1]))
    print("{}".format(which_failed).center(30))
    
    

if __name__ == "__main__":
    
    """Some material with which to test testing."""
    
    import itertools as it

    def is_geometric_progression(array):
        """Returns if array (sorted) is a geometric progression of the form
            
                r**i, r**{i+1}, ...
        
            for nonnegative integers r and i.  I'm hoping that I don't need to 
            worry about scaling factor a.
        """
        return all([array[i+1]/array[i] == array[1]/array[0] for i in range(len(array)-1)])

    def count_geo_progs(array, r):
        count = 0
        for combo in it.combinations(array, r):
            count += is_geometric_progression(combo)
        return count

    test(count_geo_progs, [([1,4,16,64], 3)], [2])
    test(count_geo_progs, args, expected)
    

    
