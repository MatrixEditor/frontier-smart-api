package apk;

public class BaseDebugIncidentReportList extends NodeList implements NodeInfo {
  private static NodeInfo.NodePrototype Prototype;

  @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
  public boolean IsCacheable() {
      return true;
  }

  @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
  public boolean IsNotifying() {
      return false;
  }

  @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
  public boolean IsReadOnly() {
      return true;
  }

  @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
  public long getAddress() {
      return 283574272L;
  }

  @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
  public String getName() {
      return "netRemote.debug.incidentReport.list";
  }

  @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
  public NodeInfo.NodePrototype getPrototype() {
      if (Prototype == null) {
          ArrayList<NodeInfo.NodePrototype.Arg> arrayList = new ArrayList<>();
          arrayList.add(new NodeInfo.NodePrototype.Arg("uuid", NodeInfo.NodePrototype.Arg.ArgDataType.C, 100));
          arrayList.add(new NodeInfo.NodePrototype.Arg("path", NodeInfo.NodePrototype.Arg.ArgDataType.C, 100));
          arrayList.add(new NodeInfo.NodePrototype.Arg("time", NodeInfo.NodePrototype.Arg.ArgDataType.C, 100));
          arrayList.add(new NodeInfo.NodePrototype.Arg("key", NodeInfo.NodePrototype.Arg.ArgDataType.C, 100));
          Prototype = new NodeInfo.NodePrototype(arrayList);
      }
      return Prototype;
  }

  public BaseDebugIncidentReportList() {
    super();
  }
}
