package com.frontier_silicon.NetRemoteLib.Node;

import com.frontier_silicon.NetRemoteLib.Node.NodeInfo;

public class BaseDebugIncidentReportCreate extends NodeU8 implements NodeInfo {
    private static final NodeInfo.NodePrototype Prototype = new NodeInfo.NodePrototype(new NodeInfo.NodePrototype.Arg(NodeInfo.NodePrototype.Arg.ArgDataType.U8));


    @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
    public boolean IsCacheable() {
        return false;
    }

    @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
    public boolean IsNotifying() {
        return false;
    }

    @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
    public boolean IsReadOnly() {
        return false;
    }

    @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
    public long getAddress() {
        return 281026560L;
    }

    @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
    public String getName() {
        return "netRemote.debug.incidentReport.create";
    }

    @Override // com.frontier_silicon.NetRemoteLib.Node.NodeInfo
    public NodeInfo.NodePrototype getPrototype() {
        return Prototype;
    }

    public BaseDebugIncidentReportCreate(Long l) {
        super(l);
    }

}