% Knights and Knaves Puzzles Implementation in Prolog

% Puzzle 1
% A says: "We are both knaves."
% Expected Output: [a=knave, b=knight]

puzzle_1 :-
    % Assign a role to A (knight or knave)
    member(RoleA, [knight, knave]),
    % Assign a role to B (knight or knave)
    member(RoleB, [knight, knave]),
    
    % A's statement: "We are both knaves."
    % If A is a knight, the statement must be true
    % If A is a knave, the statement must be false
    (
        (RoleA = knight, RoleA = knave, RoleB = knave) ;    % Knight telling the truth (contradiction)
        (RoleA = knave, \+ (RoleA = knave, RoleB = knave))  % Knave lying about both being knaves
    ),
    
    % Output the result
    write([a=RoleA, b=RoleB]), nl,
    
    % Force backtracking to find all possible solutions
    fail.

% Puzzle 2
% A says: "At least one of us is a knave."
% Expected Output: [a=knight, b=knave]

puzzle_2 :-
    % Assign a role to A (knight or knave)
    member(RoleA, [knight, knave]),
    % Assign a role to B (knight or knave)
    member(RoleB, [knight, knave]),
    
    % A's statement: "At least one of us is a knave."
    % If A is a knight, the statement must be true
    % If A is a knave, the statement must be false
    (
        (RoleA = knight, (RoleA = knave ; RoleB = knave)) ;    % Knight telling the truth
        (RoleA = knave, \+ (RoleA = knave ; RoleB = knave))   % Knave lying
    ),
    
    % Output the result
    write([a=RoleA, b=RoleB]), nl,
    
    % Force backtracking to find all possible solutions
    fail.

% Puzzle 3
% A says: "Either I am a knave or B is a knight."
% Expected Output: [a=knight, b=knight]

puzzle_3 :-
    % Assign a role to A (knight or knave)
    member(RoleA, [knight, knave]),
    % Assign a role to B (knight or knave)
    member(RoleB, [knight, knave]),
    
    % A's statement: "Either I am a knave or B is a knight."
    % If A is a knight, the statement must be true
    % If A is a knave, the statement must be false
    (
        (RoleA = knight, (RoleA = knave ; RoleB = knight)) ;    % Knight telling the truth
        (RoleA = knave, \+ (RoleA = knave ; RoleB = knight))   % Knave lying
    ),
    
    % Output the result
    write([a=RoleA, b=RoleB]), nl,
    
    % Force backtracking to find all possible solutions
    fail.

% Puzzle 4
% A says: "We are the same."
% Expected Output: [a=knave, b=knight] or [a=knight, b=knight]

puzzle_4 :-
    % Assign a role to A (knight or knave)
    member(RoleA, [knight, knave]),
    % Assign a role to B (knight or knave)
    member(RoleB, [knight, knave]),
    
    % A's statement: "We are the same."
    % If A is a knight, the statement must be true
    % If A is a knave, the statement must be false
    (
        (RoleA = knight, RoleA = RoleB) ;        % Knight telling the truth
        (RoleA = knave, \+ (RoleA = RoleB))     % Knave lying
    ),
    
    % Output the result
    write([a=RoleA, b=RoleB]), nl,
    
    % Force backtracking to find all possible solutions
    fail.
