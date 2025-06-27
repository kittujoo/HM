namespace MillTestRest.models
{
    public record GetCellRectangleRequest
    {
        public int row { get; set; }
        public int column { get; set; }
    }
}
