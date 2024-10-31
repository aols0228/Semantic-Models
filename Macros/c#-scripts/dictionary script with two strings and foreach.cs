/*
Forfatter: Andreas Nordgaard aols0228 og ChatGPT
Link til kilde: 
Beskrivelse: Macro, that creates or updates shared expressions
    1. It creates a dictionary with key/value pairs of typestring/string with the M parameters you wish to update
    2. If the M parameters do not preexist the script fails
    3. If they exist it fetches the M parameters with the same name as in the dictionary
    3. It then insert the new parameters value for sandbox environment

Change Log: (udskift denne med dine noter)
---------------------------------------------------------------
Ver. | Dato DD-MM-YYYY | Forfatter | Beskrivelse
1.0    19-06-2024        aols0228    Frigivelse af makro

*/

var _SharedExpressions = new Dictionary<string, string>()
{
    { "insert text", "insert text" }
    // Add other entries if needed, following the format: { "Key", "Value" },
};

foreach (var _parameters in _SharedExpressions)
{
    Model.Expressions[_parameters.Key].Expression = 
        @"""" + _parameters.Value + @"""
meta [
    IsParameterQuery         = true,
    IsParameterQueryRequired = true,
    Type                     = type text
]";
}