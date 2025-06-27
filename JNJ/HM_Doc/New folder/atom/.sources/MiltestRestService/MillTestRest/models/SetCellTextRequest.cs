namespace MillTestRest.models
{
    public class SetCellTextRequest
    {
        public int row { get; set; }
        public int column { get; set; }
        public string text { get; set; } = "";
    }
}
