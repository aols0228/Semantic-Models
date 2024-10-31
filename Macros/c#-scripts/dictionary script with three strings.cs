/*
Forfatter: Andreas Nordgaard aols0228 og ChatGPT
Link til kilde: 
Beskrivelse: Macro that creates or updates shared expressions
    1. It creates a dictionary with key/value pairs of typestring/string with the M parameters you wish to update
    2. If the M parameters do not preexist the script fails
    3. If they exist it fetches the M parameters with the same name as in the dictionary
    3. It then insert the new parameters value for sandbox environment

Change Log: (udskift denne med dine noter)
---------------------------------------------------------------
Ver. | Dato DD-MM-YYYY | Forfatter | Beskrivelse
1.0    19-06-2024        aols0228    Frigivelse af makro
1.1    19-09-2024        aols0228    Brug af custom class, ExpressionInfo, for at tilføje beskrivelse
*/

public class ExpressionInfo
{
    public string Key { get; set; }
    public string Value { get; set; }
    public string Description { get; set; }
}

var Expression = new ExpressionInfo  // Add the strings directly below
{ 
    Key = "insert text", // Name of shared expression  
    Value = "insert text", // Value of --||-- 
    Description = "insert text" // Description of --||--
};

Model.Expressions[Expression.Key].Expression = 
    $@"// {Expression.Description} {Expression.Key.ToLower()}
""" + Expression.Value + @"""
meta [
    IsParameterQuery         = true,
    IsParameterQueryRequired = true,
    Type                     = type text
]";