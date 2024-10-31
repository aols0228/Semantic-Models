/*
Forfatter: Andreas Nordgaard aols0228 og ChatGPT
Link til kilde: 
Beskrivelse: Macro that creates or updates shared expressions
    1. It creates a dictionary with key/value pairs of typestring/string with the M parameters you wish to update
    2. If the M parameters do not preexist the script fails
    3. If they exist it fetches the M parameters with the same name as in the dictionary
    3. It then insert the new parameters value for sandbox environment

Change Log:
---------------------------------------------------------------
Ver. | Dato DD-MM-YYYY | Forfatter | Beskrivelse
1.0    19-06-2024        aols0228    Release af makro
1.1    19-09-2024        aols0228    Brug af custom class, ExpressionInfo, for at tilføje beskrivelse
*/

public class ExpressionInfo
{
    public string Value { get; set; }
    public string Description { get; set; }
}

var _SharedExpressions = new Dictionary<string, ExpressionInfo>()
{
    // Key: string that identifies the expression
    // Value: ExpressionInfo object containing the actual expression value and a description
    { "insert text", new ExpressionInfo { Value = "insert text", Description = "insert text" } }
    // Add other entries if needed, following the format: { "Key", new ExpressionInfo { Value = "value", Description = "description" } },
};

foreach (var entry in _SharedExpressions)
{
    var key = entry.Key; // Get the key from the dictionary
    var _parameters = entry.Value; // Get the ExpressionInfo object
    
    Model.Expressions[key].Expression = 
        $@"// {_parameters.Description} {key.ToLower()}
""" + _parameters.Value + @"""
meta [
    IsParameterQuery         = true,
    IsParameterQueryRequired = true,
    Type                     = type text
]""";
}