namespace MillTestRest.milltest
{
    using MillTestRest.models;
    using System.Drawing;
    using System.Runtime.InteropServices;
    using System.Text;
    //using Rect = Commons.Utils.TableViewSupportUtil.Rect;


    public static class MiltestDllUtil
    {
        [DllImport("miltest.dll")]
        public static extern int NumColumns(int hTable);

        [DllImport("miltest.dll")]
        public static extern int NumHiddenColumns(int hTable);

        [DllImport("miltest.dll")]
        public static extern int NumRows(int hTable);

        [DllImport("miltest.dll")]
        public static extern int GetCellText(int hTable, int iRow, int iCol, StringBuilder pText);

        [DllImport("miltest.dll")]
        public static extern int GetColumnNum(int hTable, string pText);

        [DllImport("miltest.dll")]
        public static extern int SelectRow(int hTable, int iRow);

        [DllImport("miltest.dll")]
        public static extern int SelectAndShowRow(int hTable, int iRow);

        [DllImport("miltest.dll")]
        public static extern int DeselectRow(int hTable, int iRow);

        [DllImport("miltest.dll")]
        public static extern int SetCellText(int hTable, int iRow, int iCol, string pText);

        [DllImport("miltest.dll")]
        public static extern int SelectColumn(int hTable, int iCol);

        [DllImport("miltest.dll")]
        public static extern int SelectAndShowColumn(int hTable, int iCol);

        [DllImport("miltest.dll")]
        public static extern int IsColumnHidden(int hTable, int iCol);

        [DllImport("miltest.dll")]
        public static extern int DeselectColumn(int hTable, int iCol);

        [DllImport("miltest.dll")]
        public static extern int HideColumn(int hTable, int iCol);

        [DllImport("miltest.dll")]
        public static extern int ShowColumn(int hTable, int iCol);

        [DllImport("miltest.dll")]
        public static extern int MoveColumn(int hTable, int iFromCol, int iToCol);

        [DllImport("miltest.dll")]
        public static extern int IsRowSelected(int hTable, int iRow);

        [DllImport("miltest.dll")]
        public static extern int NumSelectedRows(int hTable);

        [DllImport("miltest.dll")]
        public static extern int GetListBoxCheck(int hWnd, int iRow);

        [DllImport("miltest.dll")]
        public static extern int SetListBoxCheck(int hWnd, int iRow, bool bCheck);

        [DllImport("miltest.dll")]
        public static extern int WhereIsCell(int hTable, int iRow, int iCol, ref Rect pRect);

        [DllImport("miltest.dll")]
        public static extern int SelectTabNum(int hTab, int iTab);

        [DllImport("miltest.dll")]
        public static extern int SelectTabTitle(int hTab, string pText);

        [DllImport("miltest.dll")]
        public static extern int GetTabNum(int hTab, string pText);

        [DllImport("miltest.dll")]
        public static extern int GetTabText(int hTab, int nTab, StringBuilder pText);

        [DllImport("miltest.dll")]
        public static extern int NumTabs(int hTab);

        [DllImport("miltest.dll")]
        public static extern int GetCurrentTab(int hTab);

        [DllImport("miltest.dll")]
        public static extern int MakeCellVisible(int hTable, int iRow, int iCol);

        [DllImport("miltest.dll")]
        public static extern int IsCellFaulted(int hTable, int iRow, int iCol);
    }

}
